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

@app.get("/activities", response_model=List[schemas.Activity])
def read_all_activities(db: Session = Depends(get_db)):
    activities = crud.get_activities(db)
    return activities