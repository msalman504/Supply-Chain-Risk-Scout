from langgraph.graph import StateGraph, END
from src.models.supplier import Supplier
from src.tools.financial import fetch_financial_risk
from src.tools.esg import fetch_esg_risk
from src.tools.logistics import fetch_logistics_risk
from typing import TypedDict


class GraphState(TypedDict):
    supplier: Supplier
    scores: dict
    final_score: int


async def compute_risk(state: GraphState) -> GraphState:
    supplier = state["supplier"]
    scores = {
        "financial": await fetch_financial_risk.ainvoke({"supplier_name": supplier.name}),
        "esg": await fetch_esg_risk.ainvoke({"supplier_name": supplier.name}),
        "logistics": await fetch_logistics_risk.ainvoke({"supplier_name": supplier.name}),
    }
    final = int(
        0.4 * scores["financial"] + 0.25 * scores["logistics"] + 0.2 * scores["esg"]
    )
    return {"supplier": supplier, "scores": scores, "final_score": final}


workflow = StateGraph(GraphState)
workflow.add_node("compute", compute_risk)
workflow.set_entry_point("compute")
workflow.add_edge("compute", END)
app = workflow.compile()
