import datetime
import time
from typing import List

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



@router.get("/", response_model=List[schemas.Item])
def read_items(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    # return items
    return templates.TemplateResponse("items.html",{"request": request, "item_list": items})
