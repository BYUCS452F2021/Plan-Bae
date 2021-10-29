from .database import Base

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



