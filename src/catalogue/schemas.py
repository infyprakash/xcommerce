from typing import List,Optional
from pydantic import BaseModel,root_validator
from uuid import UUID
from datetime import datetime

# schema for product_image

class ProductImageBase(BaseModel):
    product_id: int
    image_url: str 

class ProductImageCreate(ProductImageBase):
    class Config:
        schema_extra = {
            "example":{
                "product_id": 100,
                "image_url": "test.png"
            }
        }

class ProductImageModel(ProductImageBase):
    id: int 
    uuid: UUID
    class Config:
        orm_mode = True

# schema for product
class ProductBase(BaseModel):
    name: str 
    price: float
    sku: str = None
    description: str
    category_id: int
    shop_id: int


class ProductCreate(ProductBase):
    class Config:
        schema_extra = {
            "example":{
                    "name":"Iphone",
                    "price":22000,
                    "sku": "XXXXX",
                    "description":"premium apple's Iphone13",
                    "category_id":100,
                    "shop_id":100
            }
        }

class ProductModel(ProductBase):
    id: int 
    uuid: UUID
    product_images: list[ProductImageModel] = []
    class Config:
        orm_mode = True
    
# schema for category
class CategoryBase(BaseModel):
    name: str 
    image: str
    description: str

class CategoryCreate(CategoryBase):
    class config:
        schema_extra = {
            "example":{
                    "name":"Grocery",
                    "image":"grocery.png",
                    "description":"Describe this category"
            }
        }

class CategoryModel(CategoryBase):
    id: int 
    uuid: UUID
    products: list[ProductModel] = []
    class Config:
        orm_mode = True
    




