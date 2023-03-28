import uuid
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional,List
from pydantic import BaseModel,UUID4,EmailStr
from src.core.enumerate import DistrictEnum,ProvinceEnum,BusinessTypeEnum
from src.catalogue.schemas import ProductModel

class AddressBase(BaseModel):
    country: str = 'Nepal'
    province: ProvinceEnum = None
    district: DistrictEnum = None
    municipality: str
    city_or_village: str
    ward: str
    street: str = None
    house_no: str = None

class AddressCreate(AddressBase):
    class Config:
        schema_extra = {
            "example":{
                    # "country":"Nepal",
                    "province": "Bagmati",
                    "district": "Sarlahi",
                    "municipality":"Kabilasi",
                    "city_or_village":"kabilasi",
                    "ward":"08",
                    "street":"sahid marga",
                    "house_no":"01"
            }
        }


class AddressModel(AddressBase):
    id: int
    uuid: UUID
    class Config:
        orm_mode = True

# schema for shop

class ShopBase(BaseModel):
    name: str
    business_type: BusinessTypeEnum  = None
    address: int
    phone_no: str 
    email: EmailStr
    website: str
    pan_no: str
    description: Optional[str] = "description text"
    owner_id: int


class ShopCreate(ShopBase):
    class Config:
        schema_extra = {
            "example":{
                    "name": "xyz shop",
                    "business_type": "Grocery",
                    "address": 100,
                    "phone_no": "9840143772",
                    "email": "xyz@gmail.com",
                    "website": "www.xyz.com",
                    "pan_no": "12345",
                    "description": "Describe your shop",
                    # "logo_url": "logo.png",
                    # "banner_url": "banner.png",
                    "owner_id":100
            }
        }

class ShopUpdate(ShopBase):
    id: int

class ShopModel(ShopBase):
    id: int
    uuid: Optional[uuid.UUID]
    banner_url: str 
    logo_url: str 
    products: List[ProductModel] = []

    class Config:
        orm_mode = True