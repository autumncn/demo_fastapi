from typing import List, Optional, Union
from pydantic import BaseModel, EmailStr

from db.schemas.items import Item


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    username: str
    # email: str
    email: EmailStr
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        # arbitrary_types_allowed = True
        orm_mode = True

class ShowUser(BaseModel):   #new
    username: str
    # email: str
    email: EmailStr
    is_active: bool

    class Config:  #tells pydantic to convert even non dict obj to json
        # arbitrary_types_allowed = True
        orm_mode = True