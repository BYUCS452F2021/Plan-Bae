from pydantic import Base


class Activity(Base):
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


class Date(Base):
    date_id: int 
    user_id: int 
    time: DateTime

class User(Base):
    user_id: int
    username: str 
    password: str



class DateActivity(Base):
    dateactivity_id: int
    date_id: int
    activity_id: int