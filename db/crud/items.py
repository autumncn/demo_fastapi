from fastapi import HTTPException
from sqlalchemy.orm import Session

from db.models.items import Item
from db.models.users import User
from db.schemas.items import ItemCreate
from db.schemas.users import UserCreate


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: ItemCreate, user_id: int):
    db_item = Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
