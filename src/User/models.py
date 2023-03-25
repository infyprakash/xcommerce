from sqlalchemy import Column,Boolean,Integer,String,Float,Unicode,DateTime,ForeignKey,Date
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from src.db.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_no = Column(String, unique=True, index=True)
    date_of_birth = Column(Date,nullable=True,default='2050-01-01')
    hashed_password = Column(String)
    is_superuser = Column(Boolean, default=False)
    is_staff = Column(Boolean,default=False)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,nullable=False,default=datetime.utcnow())
    updated_at = Column(DateTime,nullable=False,default=datetime.utcnow())
    
    shop = relationship('Shop',back_populates='owner')

