import datetime
import time

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db import schemas, crud
from db.database import get_db
from db.schemas.items import ItemCreate, Item
from db.schemas.users import UserCreate, User
from db.repository.users import create_new_user
from logs.logger import logger

router = APIRouter()


@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user


@router.post("/create", response_model=User)
def create_user_detail(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/{user_id}/items/", response_model=Item)
def create_item_for_user(
        user_id: int, item: ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)
