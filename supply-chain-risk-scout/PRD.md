# Supply-Chain Risk Scout — Product Requirements Document (PRD)
Version: 1.0  
Author: <your-name>  
Last Updated: 2025-07-21

## 1. Vision
Build an AI agent that continuously monitors a company’s supplier list, flags emerging risks (financial, geopolitical, ESG, logistics), and produces **actionable daily briefs** plus **on-demand deep-dive PDF reports**.

## 2. Target Market & Users
- Primary: Mid-market manufacturers & e-commerce operators (50-500 suppliers).  
- Secondary: Procurement consultants, PE due-diligence teams.

## 3. Jobs-to-be-Done
1. **“I need to know if any of my suppliers are about to fail financially.”**  
2. **“I need an early warning when a port strike will delay my components.”**  
3. **“I need evidence for auditors that we monitor ESG compliance.”**

## 4. Core Features
| Feature | MVP | v1.1 |
|---------|-----|------|
| Supplier onboarding (CSV or API) | ✅ | ✅ |
| Real-time risk monitoring (financial, geo, ESG) | ✅ | ✅ |
| Daily Slack / Teams digest | ✅ | ✅ |
| Interactive dashboard (Streamlit) | ✅ | ✅ |
| PDF risk report generator | ✅ | ✅ |
| Scenario simulation (what-if) | ❌ | ✅ |
| Supplier scorecard API | ❌ | ✅ |

## 5. Data Sources
- **Financial**: RapidAPI (Yahoo Finance), Creditsafe, OpenCorporates.  
- **Geopolitical**: GDELT, PortStrike RSS, NOAA weather alerts.  
- **ESG**: Sustainalytics API, CDP disclosures.  
- **Logistics**: MarineTraffic API, Flexport webhooks.  
- **News & Social**: Tavily, GDELT 2.0, Twitter v2 filtered stream.

## 6. Risk Scoring Logic
- **0-100 composite score** (higher = riskier).  
- Weightings: 40 % Financial, 25 % Geopolitical, 20 % ESG, 15 % Logistics.  
- Thresholds:  
  - Green ≤ 30  
  - Amber 31-60  
  - Red > 60

## 7. User Flow
1. Upload supplier master list (CSV).  
2. Agent ingests → enriches → calculates risk scores.  
3. Slack digest delivered every 24 h.  
4. User clicks “Generate Report” → 3-page PDF in <60 s.

## 8. Non-functional
- **Latency**: Slack digest <30 s after trigger.  
- **Scalability**: 10 k suppliers per tenant.  
- **Security**: SOC-2 Type II controls, AES-256 at rest, TLS 1.3 in transit.  
- **Compliance**: GDPR, CCPA (right-to-delete via `/forget-supplier` endpoint).

## 9. Tech Stack
- **LangGraph** for orchestration.  
- **LangChain** for retrieval, tools, LLM chains.  
- **Pydantic** for data validation.  
- **FastAPI** for REST endpoints.  
- **Streamlit** for dashboard.  
- **PostgreSQL** (state), **Redis** (cache), **S3** (reports).  
- **LangSmith** for observability.

## 10. Success Metrics (first 90 days)
- **Activation**: 80 % of sign-ups upload ≥1 supplier list.  
- **Retention**: 60 % weekly active tenants at day 30.  
- **Value**: ≥2 risk incidents caught per tenant per month.  
- **Revenue**: $10 k MRR by day 90.

## 11. Pricing
- **Starter** (≤50 suppliers): $99/mo  
- **Growth** (≤500 suppliers): $299/mo  
- **Enterprise** (unlimited): Custom

## 12. Open Questions
- Do we store **PII** of supplier contacts? → Decision: No, only public identifiers.  
- Do we allow **white-label** PDF? → Decision: Enterprise tier only.