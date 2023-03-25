import uuid
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional,List
from pydantic import BaseModel,UUID4
from src.core.enumerate import DistrictEnum,ProvinceEnum
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
    address: int
    pan_no: str
    owner_id: int
    description: Optional[str] = "description text"

class ShopCreate(ShopBase):
    class Config:
        schema_extra = {
            "example":{
                    "name": "xyz shop",
                    "address": 100,
                    "pan_no": "12345",
                    "description": "Describe your shop",
                    "owner_id":100
            }
        }


class ShopModel(ShopBase):
    id: int
    uuid: Optional[uuid.UUID]
    products: List[ProductModel] = []

    class Config:
        orm_mode = True