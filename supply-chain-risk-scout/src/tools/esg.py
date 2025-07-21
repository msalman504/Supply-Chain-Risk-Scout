import httpx
import os
from langchain.tools import tool
from pydantic import BaseModel, Field


class ESGInput(BaseModel):
    supplier_name: str = Field(..., description="Official company name")


@tool(args_schema=ESGInput)
async def fetch_esg_risk(supplier_name: str) -> int:
    """Return 0-100 ESG risk score via Sustainalytics API."""
    url = f"https://api.sustainalytics.com/v1/companies?name={supplier_name}"
    headers = {"Authorization": f"Bearer {os.getenv('SUSTAINALYTICS_KEY')}"}
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(url, headers=headers)
            r.raise_for_status()
            data = r.json()
        # Adjust this line to match the real Sustainalytics API response structure
        risk_score = int(data["companies"][0]["esgRiskScore"])
        return risk_score
    except Exception as e:
        print(f"Error fetching ESG risk: {e}")
        return 100
