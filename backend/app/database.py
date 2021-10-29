import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

hostname = os.environ["DB_HOSTNAME"]
port = os.environ["DB_PORT"]
username = os.environ["DB_USERNAME"]
password = os.environ["DB_PASSWORD"]
database_name = os.environ["DB_NAME"]

DATABASE_URL = f"mysql+pymysql://{username}:{password}@{hostname}:{port}/{database_name}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()