from pydantic import BaseModel, Field, AnyHttpUrl
from typing import Optional
from datetime import datetime


class Supplier(BaseModel):
    id: str
    name: str
    country: str
    industry: str
    website: Optional[AnyHttpUrl] = None
    risk_score: Optional[int] = Field(ge=0, le=100, default=None)
    last_updated: Optional[datetime] = None
