import streamlit as st
import httpx
from src.models.supplier import Supplier

st.title("Supply-Chain Risk Scout")

name = st.text_input("Supplier name")
country = st.text_input("Country")
industry = st.text_input("Industry")
website = st.text_input("Website (optional)")

if st.button("Run"):
    supplier = Supplier(id="tmp", name=name, country=country, industry=industry, website=website)
    r = httpx.post(
        "http://localhost:8000/score",
        json=supplier.model_dump(mode="json"),
        headers={"X-API-Key": "my-placeholder-key"}
    )
    st.json(r.json())
