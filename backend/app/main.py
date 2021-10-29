import os
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

import crud, models, schemas
from database import SessionLocal, engine

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


'''
GET Endpoints
'''

# Get all activities
@app.get("/activities", response_model=List[schemas.Activity], tags=["Activities"])
def read_all_activities(db: Session = Depends(get_db)):
    activities = crud.get_activities(db)
    return activities

# Get specific activity by ID
@app.get("/activities/id/{activity_id}", response_model=schemas.Activity, tags=["Activities"])
def read_activity(activity_id: int, db: Session = Depends(get_db)):
    activity = crud.get_activity(db, activity_id)
    return activity

# Get specific activity by name
@app.get("/activities/name/{activity_name}", response_model=schemas.Activity, tags=["Activities"])
def read_activity(activity_name: str, db: Session = Depends(get_db)):
    activity = crud.get_activity_by_name(db, activity_name)
    return activity

# Get all users
@app.get("/users", response_model=List[schemas.User], tags=["Users"])
def read_all_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

# Get specific user by ID
@app.get("/users/id/{user_id}", response_model=schemas.User, tags=["Users"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    return user

# Get specific user by username
@app.get("/users/username/{username}", response_model=schemas.User, tags=["Users"])
def read_user(username: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username)
    return user

# Get all dates
@app.get("/dates", response_model=List[schemas.Date], tags=["Dates"])
def read_all_dates(db: Session = Depends(get_db)):
    dates = crud.get_dates(db)
    return dates

# Get specific date by ID
@app.get("/dates/{date_id}", response_model=schemas.Date, tags=["Dates"])
def read_date(date_id: int, db: Session = Depends(get_db)):
    date = crud.get_date(db, date_id)
    return date

# Get all dates for a particular user
@app.get("/dates/user/{user_id}", response_model=List[schemas.Date], tags=["Dates", "Users"])
def read_user_dates(user_id: int, db: Session = Depends(get_db)):
    dates = crud.get_user_dates(db, user_id)
    return dates

# Get all date activities
@app.get("/dateactivities", response_model=List[schemas.DateActivity], tags=["DateActivities"])
def read_all_dateactivities(db: Session = Depends(get_db)):
    dateactivities = crud.get_dateactivities(db)
    return dateactivities

# Get specific date activity by ID
@app.get("/dateactivities/{dateactivity_id}", response_model=schemas.DateActivity, tags=["DateActivities"])
def read_dateactivity(dateactivity_id: int, db: Session = Depends(get_db)):
    dateactivity = crud.get_dateactivity(db, dateactivity_id)
    return dateactivity

# Get all date activities for a particular date
@app.get("/dateactivities/date/{date_id}", response_model=List[schemas.DateActivity], tags=["DateActivities"])
def read_date_dateactivities(date_id: int, db: Session = Depends(get_db)):
    dateactivities = crud.get_date_dateactivities(db, date_id)
    return dateactivities


'''
Post Endpoints
'''

# Create new activity
@app.post("/activity/", response_model=schemas.Activity, tags=["Activities"])
def create_activity(activity: schemas.ActivityCreate, db: Session = Depends(get_db)):
    db_activity = crud.get_activity_by_name(db, activity.name)
    if db_activity:
        raise HTTPException(status_code=400, detail="Activity with that name already exists")
    return crud.create_activity(db, activity)

# Create new activities
@app.post("/activities/", response_model=List[schemas.Activity], tags=["Activities"])
def create_activities(activities: List[schemas.ActivityCreate], db: Session = Depends(get_db)):
    return crud.create_activities(db, [activity for activity in activities if not crud.get_activity_by_name(db, activity.name)])

# Create new user
@app.post("/user/", response_model=schemas.User, tags=["Users"])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already in use")
    return crud.create_user(db, user)

# Create new users
@app.post("/users/", response_model=List[schemas.User], tags=["Users"])
def create_users(users: List[schemas.UserCreate], db: Session = Depends(get_db)):
    return crud.create_users(db, [user for user in users if not crud.get_user_by_username(db, user.username)])

# Create new date
@app.post("/date/", response_model=schemas.Date, tags=["Dates"])
def create_date(date: schemas.DateCreate, db: Session = Depends(get_db)):
    return crud.create_date(db, date)

# Create new dates
@app.post("/dates/", response_model=List[schemas.Date], tags=["Dates"])
def create_dates(dates: List[schemas.DateCreate], db: Session = Depends(get_db)):
    return crud.create_dates(db, dates)

# Create new date activity
@app.post("/dateactivity/", response_model=schemas.DateActivity, tags=["DateActivities"])
def create_dateactivity(dateactivity: schemas.DateActivityCreate, db: Session = Depends(get_db)):
    return crud.create_dateactivity(db, dateactivity)

# Create new date activities
@app.post("/dateactivities/", response_model=List[schemas.DateActivity], tags=["DateActivities"])
def create_dateactivities(dateactivities: List[schemas.DateActivityCreate], db: Session = Depends(get_db)):
    return crud.create_dateactivities(db, dateactivities)


'''
Delete Endpoints
'''

# Delete an activity
@app.delete("/activity/", response_model=schemas.DeleteResponse, tags=["Activities"])
def delete_activity(activity_id: int, db: Session = Depends(get_db)):
    return crud.delete_activity(db, activity_id)

# Delete activities
@app.delete("/activities/", response_model=schemas.DeleteResponse, tags=["Activities"])
def delete_activities(activity_ids: List[int], db: Session = Depends(get_db)):
    return crud.delete_activities(db, activity_ids)

# Delete a user
@app.delete("/user/", response_model=schemas.DeleteResponse, tags=["Users"])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)

# Delete users
@app.delete("/users/", response_model=schemas.DeleteResponse, tags=["Users"])
def delete_users(user_ids: List[int], db: Session = Depends(get_db)):
    return crud.delete_users(db, user_ids)

# Delete a date
@app.delete("/date/", response_model=schemas.DeleteResponse, tags=["Dates"])
def delete_date(date_id: int, db: Session = Depends(get_db)):
    return crud.delete_date(date_id)

# Delete dates
@app.delete("/dates/", response_model=schemas.DeleteResponse, tags=["Dates"])
def delete_dates(date_ids: List[int], db: Session = Depends(get_db)):
    return crud.delete_dates(db, date_ids)

# Delete a dateactivity
@app.delete("/dateactivity/", response_model=schemas.DeleteResponse, tags=["DateActivities"])
def delete_dateactivity(dateactivity_id: int, db: Session = Depends(get_db)):
    return crud.delete_dateactivity(dateactivity_id)

# Delete dateactivities
@app.delete("/dateactivities/", response_model=schemas.DeleteResponse, tags=["DateActivities"])
def delete_dateactivities(dateactivity_ids: List[int], db: Session = Depends(get_db)):
    return crud.delete_dateactivities(db, dateactivity_ids)
