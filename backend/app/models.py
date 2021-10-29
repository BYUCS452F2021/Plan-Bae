from .database import Base
from pydantic import BaseModel

class Activity(Base):
    __tablename__ = "Activity"
    activity_id = Column(Integer, unique = True, primary_key = True)
    name = Column(String)
    tags = Column(String)
    active = Column(Integer)
    description = Column(String)
    url = Column(String)
    min_cost = Column(Integer)
    duration = Column(Integer)
    latitude = Column(String)
    longitude = Column(String)

class Date(Base):
    __tablename__ = "Date"
    date_id = Column(Integer, unique=True,primary_key = True)
    user_id = Column(Integer, unique = True)
    time = Column(DateTime)

class User(Base):
    __tablename__ = "User"
    user_id = Column(Integer, unique=True, primary_key = True)
    username = Column(String)
    password = Column(String)

class DateActivity(Base):
    __tablename__ = "DateActivity"
    dateactivity_id = Column(Integer, unique = True, primary_key = True)
    date_id = Column(Integer)
    activity_id = Column(Integer)


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
