from pydantic import BaseModel
from uuid import UUID

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


# schema for product
class ProductBase(BaseModel):
    name: str 
    price: float
    image: str
    description: str

class ProductCreate(ProductBase):
    class config:
        schema_extra = {
            "example":{
                    "name":"Iphone",
                    "price":22000,
                    "image":"test.png",
                    "description":"premium apple's Iphone13"
            }
        }

class ProductModel(ProductBase):
    id: int 
    uuid: UUID

