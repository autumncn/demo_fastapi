import pymysql
pymysql.install_as_MySQLdb()  # 为了兼容mysqldb
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator            #new
from core.config import settings

# SQLALCHEMY_DATABASE_URI = "mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8".format("root", "Dreamfuture88", "localhost", "50000", "panda")
SQLALCHEMY_DATABASE_URI = settings.SQL_DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db() -> Generator:   #new
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()