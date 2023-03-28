from sqlalchemy import Column,Boolean,Integer,String,Float,Unicode,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from src.db.database import Base
from datetime import datetime

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer,primary_key=True,index=True)
    uuid = Column(UUID(as_uuid=True),unique=True,index=True,default=uuid4)
    name = Column(String,nullable=False,default='This is a sample product name')
    image = Column(String,nullable=False)
    description = Column(Unicode,default="description text")
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,nullable=False,default=datetime.utcnow())
    updated_at = Column(DateTime,nullable=False,default=datetime.utcnow())
    products = relationship('Product',back_populates='category')

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer,primary_key=True,index=True)
    uuid = Column(UUID(as_uuid=True),unique=True,index=True,default=uuid4)
    name = Column(String,nullable=False,default='This is a sample product name')
    price = Column(Float,nullable=False,default=0.00)
    # image_url = Column(String,nullable=False)
    sku = Column(String,nullable=True)
    description = Column(Unicode,default="description text")
    available = Column(Boolean,default=True)
    quantity = Column(Float,default=0.0)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,nullable=False,default=datetime.now())
    updated_at = Column(DateTime,nullable=False,default=datetime.now())
    category_id = Column(Integer,ForeignKey('categories.id'))
    shop_id = Column(Integer,ForeignKey('shops.id'))

    
    category = relationship('Category',back_populates='products')
    product_images = relationship('ProductImage',back_populates='products')
    shop = relationship('Shop',back_populates='products')

    
    __mapper_args__ = {
        "eager_defaults": True,
        "confirm_deleted_rows": False,
    }

class ProductImage(Base):
    __tablename__ = 'product_images'
    
    id = Column(Integer,primary_key=True,index=True)
    uuid = Column(UUID(as_uuid=True),unique=True,index=True,default=uuid4)
    product_id = Column(Integer,ForeignKey('products.id'))
    image_url = Column(String,nullable=False)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,nullable=False,default=datetime.now())
    updated_at = Column(DateTime,nullable=False,default=datetime.now())
    
    products = relationship('Product',back_populates='product_images')






