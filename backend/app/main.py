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
@app.get("/activities/{activity_id}", response_model=schemas.Activity)
def read_activity(activity_id: int, db: Session = Depends(get_db)):
    activity = crud.get_activity(db, activity_id)
    return activity

# Get all users
@app.get("/users", response_model=List[schemas.User])
def read_all_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

# Get specific user
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    return user

# Get all dates
@app.get("/dates", response_model=List[schemas.Date])
def read_all_dates(db: Session = Depends(get_db)):
    dates = crud.get_dates(db)
    return dates

# Get specific date
@app.get("/dates/{date_id}", response_model=schemas.Date)
def read_date(date_id: int, db: Session = Depends(get_db)):
    date = crud.get_date(db, date_id)
    return date

# Get all dates for a particular user
@app.get("/dates/user/{user_id}", response_model=List[schemas.Date])
def read_user_dates(user_id: int, db: Session = Depends(get_db)):
    dates = crud.get_user_dates(db, user_id)
    return dates

# Get all date activities
@app.get("/dateactivities", response_model=List[schemas.DateActivity])
def read_all_dateactivities(db: Session = Depends(get_db)):
    dateactivities = crud.get_dateactivities(db)
    return dateactivities

# Get specific date activity
@app.get("/dateactivities/{dateactivity_id}", response_model=schemas.DateActivity)
def read_dateactivity(dateactivity_id: int, db: Session = Depends(get_db)):
    dateactivity = crud.get_dateactivity(db, dateactivity_id)
    return dateactivity

# Get all date activities for a particular date
@app.get("/dateactivities/date/{date_id}", response_model=List[schemas.DateActivity])
def read_date_dateactivities(date_id: int, db: Session = Depends(get_db)):
    dateactivities = crud.get_date_dateactivities(db, date_id)
    return dateactivities
