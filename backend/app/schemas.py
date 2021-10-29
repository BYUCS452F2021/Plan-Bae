from pydantic import BaseModel
from datetime import datetime

class Activity(BaseModel):
    activity_id: int
    name: str
    tags: str
    active: str
    description: str
    url: str
    min_cost: int
    duration: int
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


class Date(BaseModel):
    date_id: int 
    user_id: int 
    time: datetime

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    user_id: str
    username: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class DateActivity(BaseModel):
    dateactivity_id: int
    date_id: int
    activity_id: int

    class Config:
        orm_mode = True
