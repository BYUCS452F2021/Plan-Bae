from sqlalchemy.orm import Session
from typing import List

import models, schemas

def get_activities(db: Session):
    return db.query(models.Activity).all()

def get_activity(db: Session, activity_id: int):
    return db.query(models.Activity).filter(models.Activity.activity_id == activity_id).first()

def get_activity_by_name(db: Session, name: str):
    return db.query(models.Activity).filter(models.Activity.name == name).first()

def get_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_dates(db: Session):
    return db.query(models.Date).all()

def get_date(db: Session, date_id: int):
    return db.query(models.Date).filter(models.Date.date_id == date_id).first()

def get_user_dates(db: Session, user_id: int):
    return db.query(models.Date).filter(models.Date.user_id == user_id).all()

def get_dateactivities(db: Session):
    return db.query(models.DateActivity).all()

def get_dateactivity(db: Session, dateactivity_id: int):
    return db.query(models.DateActivity).filter(models.DateActivity.dateactivity_id == dateactivity_id).first()

def get_date_dateactivities(db: Session, date_id: int):
    return db.query(models.DateActivity).filter(models.DateActivity.date_id == date_id).all()


def create_activity(db: Session, activity: schemas.ActivityCreate):
    db_activity = models.Activity(**activity.dict())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity

def create_activities(db: Session, activities: List[schemas.ActivityCreate]):
    return [create_activity(db, activity) for activity in activities]

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_users(db: Session, users: List[schemas.UserCreate]):
    return [create_user(db, user) for user in users]

def create_date(db: Session, date: schemas.DateCreate):
    db_date = models.Date(**date.dict())
    db.add(db_date)
    db.commit()
    db.refresh(db_date)
    return db_date

def create_dates(db: Session, dates: List[schemas.DateCreate]):
    return [create_date(db, date) for date in dates]

def create_dateactivity(db: Session, dateactivity: schemas.DateActivityCreate):
    db_dateactivity = models.DateActivity(**dateactivity.dict())
    db.add(db_dateactivity)
    db.commit()
    db.refresh(db_dateactivity)
    return db_dateactivity

def create_dateactivities(db: Session, dateactivities: List[schemas.DateActivityCreate]):
    return [create_dateactivity(db, dateactivity) for dateactivity in dateactivities]


def delete_activity(db: Session, activity_id: int):
    records_removed = db.query(models.Activity).filter(models.Activity.activity_id == activity_id).delete()
    db.commit()
    return records_removed

def delete_activities(db: Session, activity_ids: List[int]):
    return sum([delete_activity(db, activity_id) for activity_id in activity_ids])

def delete_user(db: Session, user_id: int):
    delete_dates(db, get_user_dates(db, user_id))
    records_removed = db.query(models.User).filter(models.User.user_id == user_id).delete()
    db.commit()
    return records_removed

def delete_users(db: Session, user_ids: List[int]):
    return sum([delete_user(db, user_id) for user_id in user_ids])

def delete_date(db: Session, date_id: int):
    delete_dateactivities(db, get_date_dateactivities(db, date_id))
    records_removed = db.query(models.Date).filter(models.Date.date_id == date_id).delete()
    db.commit()
    return records_removed

def delete_dates(db: Session, date_ids: List[int]):
    return sum([delete_date(db, date_id) for date_id in date_ids])

def delete_dateactivity(db: Session, dateactivity_id: int):
    records_removed = db.query(models.DateActivity).filter(models.DateActivity.dateactivity_id == dateactivity_id).delete()
    db.commit()
    return records_removed

def delete_dateactivities(db: Session, dateactivity_ids: List[int]):
    return sum([delete_dateactivity(db, dateactivity_id) for dateactivity_id in dateactivity_ids])
