import os
import sqlalchemy as db

hostname = os.environ["DB_HOSTNAME"]
port = os.environ["DB_PORT"]
username = os.environ["DB_USERNAME"]
password = os.environ["DB_PASSWORD"]
database_name = os.environ["DB_NAME"]

DATABASE_URL = f"mysql+pymysql://{username}:{password}@{hostname}:{port}/{database_name}"
engine = db.create_engine(DATABASE_URL)
SessionLocal = db.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = db.ext.declarative.declarative_base()