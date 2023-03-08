import datetime
import time
from typing import List
from fastapi.params import Form
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db import schemas, crud
from db.database import get_db
from dependencies import templates
from logs.logger import logger

router = APIRouter()


@router.get("/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item_view.html", {"request": request, "id": id})

@router.post("/create", response_model=schemas.Item)
async def create_item(
    set_user_id: int = Form(...),
    set_title: str = Form(...),
    set_description: str = Form(...),
    db: Session = Depends(get_db)
):
    print(set_user_id, set_title, set_description)
    new_item = schemas.ItemCreate(
            title=set_title,
            description=set_description
        )
    crud.create_user_item(db=db, item=new_item, user_id=set_user_id)
    request = Request
    return read_items(request=request, skip=0, limit=100, db=db)

@router.get("/", response_model=List[schemas.Item])
def read_items(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    # return items
    new_item = schemas.ItemCreate
    return templates.TemplateResponse("items.html",{"request": request, "item_list": items, "new_item": new_item})
