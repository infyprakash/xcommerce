import uuid
from typing import Optional,List
from datetime import date, datetime
from pydantic import BaseModel
from src.showroom.schemas import ShopModel

class UserBase(BaseModel):
    full_name: Optional[str]
    email: str
    phone_no: str
    date_of_birth: Optional[date] = date(2050, 1, 1)

class UserCreate(UserBase):
    email: str
    hashed_password: str
    # class Config:
    #     schema_extra = {
    #         "example":{
    #             "email":"xyz@gmail.com",
    #             "password":"12@qwe"
    #         }
    #     }

class UserUpdate(UserBase):
    pass 

class UserModel(UserBase):
    id: int
    uuid: Optional[uuid.UUID]
    shop: List[ShopModel] = []

    class Config:
        orm_mode = True