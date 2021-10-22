import os
from typing import Optional

from fastapi import FastAPI
import sqlalchemy as db

hostname = os.environ["DB_HOSTNAME"]
port = os.environ["DB_PORT"]
username = os.environ["DB_USERNAME"]
password = os.environ["DB_PASSWORD"]
database_name = os.environ["DB_NAME"]

engine = db.create_engine(f"mysql+pymysql://{username}:{password}@{hostname}:{port}/{database_name}")
connection = engine.connect()
metadata = db.MetaData()
activity = db.Table("Activity", metadata, autoload=True, autoload_with=engine)

# API documentation: https://fastapi.tiangolo.com
# SQLAlchemy (ORM) tutorial: https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/activities")
def read_all_activities():
    query = activity.select()
    query_result = connection.execute(query)
    activities = [res._asdict() for res in query_result]
    return activities

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}