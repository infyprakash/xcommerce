from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, ForeignKey, Unicode
from sqlalchemy.orm import relationship
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


class Shop(Base):
    __tablename__ = 'shops'
    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True),unique=True,index=True,default=uuid4)
    name = Column(String,nullable=False,default='Your shop name')
    address = Column(Integer,ForeignKey('addresses.id'))
    pan_no = Column(String,nullable=False,default='123456')
    description = Column(Unicode,default="description text")
    owner_id = Column(Integer,ForeignKey('users.id'))
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,nullable=False,default=datetime.utcnow())
    updated_at = Column(DateTime,nullable=False,default=datetime.utcnow())
    
    owner = relationship('User',back_populates='shop')
    products = relationship('Product',back_populates='shop')



