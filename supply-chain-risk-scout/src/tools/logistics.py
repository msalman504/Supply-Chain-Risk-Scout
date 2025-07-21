import httpx
import os
from langchain.tools import tool
from pydantic import BaseModel, Field


class LogisticsInput(BaseModel):
    supplier_name: str = Field(..., description="Official company name")


@tool(args_schema=LogisticsInput)
async def fetch_logistics_risk(supplier_name: str) -> int:
    """Return 0-100 logistics risk score via MarineTraffic API."""
    url = f"https://services.marinetraffic.com/api/exportvessel/v:5/{os.getenv('MARINETRAFFIC_KEY')}/timespan:60/protocol/jsono"
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(url)
            r.raise_for_status()
            data = r.json()
        # Adjust this line to match the real MarineTraffic API response structure
        risk_score = int(data["vessels"][0]["logisticsRiskScore"])
        return risk_score
    except Exception as e:
        print(f"Error fetching logistics risk: {e}")
        return 100
