import httpx
import os
from langchain.tools import tool
from pydantic import BaseModel, Field


class FinancialInput(BaseModel):
    supplier_name: str = Field(..., description="Official company name")


@tool(args_schema=FinancialInput)
async def fetch_financial_risk(supplier_name: str) -> int:
    """Return 0-100 financial risk score via Creditsafe."""
    url = f"https://connect.creditsafe.com/v1/companies?name={supplier_name}"
    headers = {"Authorization": f"Bearer {os.getenv('CREDITSAFE_KEY')}"}
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(url, headers=headers)
            r.raise_for_status()
            data = r.json()
        # Adjust this line to match the real Creditsafe API response structure
        risk_score = int(data["companies"][0]["creditScore"]["value"])
        return risk_score
    except Exception as e:
        print(f"Error fetching financial risk: {e}")
        return 100
