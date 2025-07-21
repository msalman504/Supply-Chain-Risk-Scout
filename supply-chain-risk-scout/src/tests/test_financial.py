import pytest
from src.tools.financial import fetch_financial_risk


@pytest.mark.asyncio
async def test_fetch_financial_risk(monkeypatch):
    async def mock_coroutine(supplier_name: str):
        return 42
    monkeypatch.setattr(fetch_financial_risk, "coroutine", mock_coroutine)
    result = await fetch_financial_risk.ainvoke({"supplier_name": "Acme Corp"})
    assert isinstance(result, int)
    assert 0 <= result <= 100
