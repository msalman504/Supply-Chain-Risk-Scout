from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./supplychain.db")
engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

class SupplierDB(Base):
    __tablename__ = "suppliers"
    id = Column(String, primary_key=True)
    name = Column(String)
    country = Column(String)
    industry = Column(String)
    website = Column(String)
    risk_score = Column(Integer) 