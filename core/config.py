import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "demo_fastapi"
    PROJECT_VERSION: str = "1.0.0"
    SQL_USER: str = os.getenv("SQL_USER")
    SQL_PASSWORD: str = os.getenv("SQL_PASSWORD")
    SQL_SERVER: str = os.getenv("SQL_SERVER")
    SQL_PORT: str = os.getenv("SQL_PORT")
    SQL_DB: str = os.getenv("SQL_DB")
    SQL_DATABASE_URL = "mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8".format(SQL_USER, SQL_PASSWORD, SQL_SERVER, SQL_PORT, SQL_DB)

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    ROOT_DIR = BASE_DIR[:BASE_DIR.find(PROJECT_NAME)+len(PROJECT_NAME)]

    SECRET_KEY: str = os.getenv("SECRET_KEY")  # new
    ALGORITHM = "HS256"  # new
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # in mins  #new


settings = Settings()
