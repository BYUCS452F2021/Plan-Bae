from sqlalchemy.orm import Session

import models

def get_activities(db: Session):
    return db.query(models.Activity).all()

def get_activity(db: Session, activity_id: int):
    return db.query(models.Activity).filter(models.Activity.activity_id == activity_id).first()

def get_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

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
