from fastapi import UploadFile,File
from typing import List,Optional
from pydantic import BaseModel,root_validator
from uuid import UUID
from datetime import datetime

# schema for product_image

class ProductImageBase(BaseModel):
    product_id: int
    # image_url: str 

class ProductImageCreate(ProductImageBase):
    pass
    # class Config:
    #     schema_extra = {
    #         "example":{
    #             "product_id": 100,
    #             "image_url": "test.png"
    #         }
    #     }
class ProductImageUpdate(ProductImageBase):
    id: int 

class ProductImageModel(ProductImageBase):
    id: int 
    uuid: UUID
    image_url: str 
    class Config:
        orm_mode = True

# schema for product
class ProductBase(BaseModel):
    name: str 
    price: float
    sku: str = None
    description: str
    available: bool = True
    quantity:float = 0.0
    shop_id: int


class ProductCreate(ProductBase):
    class Config:
        schema_extra = {
            "example":{
                    "name":"Iphone",
                    "price":22000,
                    "sku": "XXXXX",
                    "description":"premium apple's Iphone13",
                    "available": True,
                    "quantity": 100,
                    # "category_id":100,
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
# class CategoryBase(BaseModel):
#     name: str 
#     # image: str
#     description: str

# class CategoryCreate(CategoryBase):
#     pass
#     # class config:
#     #     schema_extra = {
#     #         "example":{
#     #                 "name":"Grocery",
#     #                 # "image":"grocery.png",
#     #                 "description":"Describe this category"
#     #         }
#     #     }
# class CategoryUpdate(CategoryBase):
#     id: int 

# class CategoryModel(CategoryBase):
#     id: int 
#     image: str 
#     uuid: UUID
#     products: list[ProductModel] = []
#     class Config:
#         orm_mode = True
    




