from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader
from src.agents.risk_pipeline import app as graph_app
from src.models.supplier import Supplier
from src.models.supplier_db import SupplierDB, async_session, Base, engine
import asyncio

api = FastAPI()

api_key_header = APIKeyHeader(name="X-API-Key")

def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != "my-placeholder-key":
        raise HTTPException(status_code=403, detail="Invalid API Key")

@api.get("/")
async def root():
    return {"message": "Supply-Chain Risk Scout API is running."}

@api.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@api.get("/healthz")
async def healthz():
    return {"status": "ok"}

@api.post("/score")
async def score_supplier(supplier: Supplier, api_key: str = Depends(verify_api_key)):
    state = {"supplier": supplier}
    result = await graph_app.ainvoke(state)
    async with async_session() as session:
        db_supplier = SupplierDB(
            id=supplier.id,
            name=supplier.name,
            country=supplier.country,
            industry=supplier.industry,
            website=str(supplier.website) if supplier.website else None,
            risk_score=result["final_score"]
        )
        session.add(db_supplier)
        await session.commit()
    return {"supplier": result["supplier"].dict(), "final_score": result["final_score"]}
