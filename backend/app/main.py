import os
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from . import crud, models, schemas
from .database import SessionLocal, engine

# API documentation: https://fastapi.tiangolo.com
# SQLAlchemy (ORM) tutorial: https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get all activities
@app.get("/activities", response_model=List[schemas.Activity])
def read_all_activities(db: Session = Depends(get_db)):
    activities = crud.get_activities(db)
    return activities

# Get specific activity
@app.get("/activities/{activity_id}")
def read_activity(activity_id: int):
    query = activity.select(activity.c.activity_id == activity_id)
    query_result = connection.execute(query)
    activities = [res._asdict() for res in query_result]
    return activities[0] if activities else None

# Get all users
@app.get("/users")
def read_all_users():
    query = user.select()
    query_result = connection.execute(query)
    users = [res._asdict() for res in query_result]
    return users

# Get specific user
@app.get("/users/{user_id}")
def read_user(user_id: int):
    query = user.select(user.c.user_id == user_id)
    query_result = connection.execute(query)
    users = [res._asdict() for res in query_result]
    return users[0] if users else None

# Get all dates
@app.get("/dates")
def read_all_dates():
    query = date.select()
    query_result = connection.execute(query)
    dates = [res._asdict() for res in query_result]
    return dates

# Get specific date
@app.get("/dates/{date_id}")
def read_date(date_id: int):
    query = date.select(date.c.date_id == date_id)
    query_result = connection.execute(query)
    dates = [res._asdict() for res in query_result]
    return dates[0] if dates else None

# Get all dates for a particular user
@app.get("/dates/user/{user_id}")
def read_user_dates(user_id: int):
    query = date.select(date.c.user_id == user_id)
    query_result = connection.execute(query)
    dates = [res._asdict() for res in query_result]
    return dates

# Get all date activities
@app.get("/dateactivities")
def read_all_dateactivities():
    query = dateactivity.select()
    query_result = connection.execute(query)
    dateactivities = [res._asdict() for res in query_result]
    return dateactivities

# Get specific date activity
@app.get("/dateactivities/{dateactivity_id}")
def read_dateactivity(dateactivity_id: int):
    query = dateactivity.select(dateactivity.c.dateactivity_id == dateactivity_id)
    query_result = connection.execute(query)
    dateactivities = [res._asdict() for res in query_result]
    return dateactivities[0] if dateactivities else None

# Get all date activities for a particular date
@app.get("/dateactivities/date/{date_id}")
def read_date_dateactivities(date_id: int):
    query = dateactivity.select(dateactivity.c.date_id == date_id)
    query_result = connection.execute(query)
    dateactivities = [res._asdict() for res in query_result]
    return dateactivities
