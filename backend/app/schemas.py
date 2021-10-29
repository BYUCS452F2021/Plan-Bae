from pydantic import BaseModel
from datetime import datetime

class ActivityBase(BaseModel):
    name: str
    tags: str
    active_level: int
    activity_description: str
    url: str
    cost: int
    duration: int
    latitude: str
    longitude: str


class ActivityCreate(ActivityBase):
    pass


class Activity(ActivityBase):
    activity_id: int

    class Config:
        orm_mode = True


class DateBase(BaseModel):
    user_id: int 
    time: datetime


class DateCreate(DateBase):
    pass


class Date(DateBase):
    date_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    user_id: str


class DateActivityBase(BaseModel):
    date_id: int
    activity_id: int


class DateActivityCreate(DateActivityBase):
    pass


class DateActivity(DateActivityBase):
    dateactivity_id: int

    class Config:
        orm_mode = True
