# Supply-Chain Risk Scout

Supply-Chain Risk Scout is an AI-powered tool for monitoring and scoring supplier risk. It helps procurement and risk teams identify high-risk suppliers by aggregating data from financial, ESG, and logistics sources. The app provides an interactive dashboard for entering supplier information and viewing risk scores, and a FastAPI backend that calculates and stores results.

**How it works:**
- When you enter a supplier, the backend fetches risk data from real external APIs (Creditsafe for financial, Sustainalytics for ESG, MarineTraffic for logistics) using your API keys.
- The backend combines these scores using a weighted formula to produce a final risk score (0-100).
- All supplier data and scores are stored in a local SQLite database.
- The dashboard (Streamlit) lets you interactively submit suppliers and view results.

**Tech stack:**
- Python 3.11, FastAPI, Streamlit, SQLAlchemy (async), SQLite
- Integrates with Creditsafe, Sustainalytics, and MarineTraffic APIs
- Uses environment variables for all secrets and API keys

## Features
- Upload and score suppliers on financial, ESG, and logistics risk
- Interactive dashboard (Streamlit)
- FastAPI backend with SQLite storage
- Pluggable for real external risk APIs

## Quick Start

1. **Clone the repo and install dependencies:**
   ```sh
   git clone <repo-url>
   cd supply-chain-risk-scout
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Set up your `.env` file:**
   - Copy `.env.example` to `.env` and fill in your API keys.

3. **Start the backend:**
   ```sh
   $env:PYTHONPATH="D:\agents\Supply-Chain Risk Scout\supply-chain-risk-scout"
   .venv\Scripts\uvicorn supply-chain-risk-scout.src.web.api:api --reload --host 0.0.0.0 --port 8000
   ```

4. **Start the dashboard:**
   ```sh
   $env:PYTHONPATH="D:\agents\Supply-Chain Risk Scout\supply-chain-risk-scout"
   .venv\Scripts\streamlit run supply-chain-risk-scout/src/web/dashboard.py --server.port 8501 --server.address 0.0.0.0
   ```

5. **Open your browser:**
   - Go to [http://localhost:8501](http://localhost:8501) to use the dashboard.

## License
MIT 
