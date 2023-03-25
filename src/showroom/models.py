from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from src.db.database import Base
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from uuid import uuid4


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True),unique=True,index=True,default=uuid4)
    country = Column(String, nullable=False,default='Nepal')
    province = Column(String,nullable=False)
    district = Column(String,nullable=False)
    municipality = Column(String, nullable=False)
    city_or_village = Column(String, nullable=False)
    ward = Column(String, nullable=False)
    street = Column(String, nullable=True)
    house_no = Column(String, nullable=True)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,nullable=False,default=datetime.utcnow())
    updated_at = Column(DateTime,nullable=False,default=datetime.utcnow())