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
    latitude = Column(Double)
    longitude = Column(Double)


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







    """
CREATE TABLE IF NOT EXISTS DateActivity (
	dateactivity_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    date_id INT NOT NULL,
    activity_id INT NOT NULL,
    FOREIGN KEY (date_id) REFERENCES Date(date_id),
    FOREIGN KEY (activity_id) REFERENCES Activity(activity_id)



    	user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(256),
	`password` VARCHAR(256),
    preferences JSON

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

    """