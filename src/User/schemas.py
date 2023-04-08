import uuid
from typing import Optional,List
from datetime import date, datetime
from pydantic import BaseModel
from src.showroom.schemas import ShopModel

class UserBase(BaseModel):
    full_name: Optional[str] = None
    email: str = None
    phone_no: str 
    date_of_birth: Optional[date] = date(2050, 1, 1)

class UserCreate(BaseModel):
    phone_no: str 
    password: str
    confirm_password: str
    class Config:
        schema_extra = {
            "example":{
                "phone_no":"9840143772",
                "password":"adminadmin",
                "confirm_password":"adminadmin"
            }
        }

class UserLogin(BaseModel):
    phone_no: str 
    password: str 
    class Config:
        schema_extra = {
            "example":{
                "phone_no":"9840143772",
                "password":"adminadmin",
            }
        }

class UserUpdate(UserBase):
    pass 

class UserModel(UserBase):
    id: int
    uuid: Optional[uuid.UUID]
    shop: List[ShopModel] = []

    class Config:
        orm_mode = True
        exclude = ('hashed_password',)