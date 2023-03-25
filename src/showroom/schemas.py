from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class AddressBase(BaseModel):
    country: str = 'Nepal'
    province: str
    district: str
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
                    "Municipality":"Kabilasi",
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