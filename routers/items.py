import datetime
import os
import time
from typing import List
from fastapi.params import Form
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import RedirectResponse, FileResponse
from starlette.background import BackgroundTask

from db import schemas, crud, models
from db.database import get_db
from db.schemas import ItemBase
from dependencies import templates
from lib.utilsJson import objetc_to_json, model_list
from logs.logger import logger

router = APIRouter()

@router.get("/", response_model=List[schemas.Item])
def read_items(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    # return items
    new_item = schemas.ItemCreate
    return templates.TemplateResponse("items.html",{"request": request, "item_list": items, "new_item": new_item})


@router.get("/id={id}", response_class=HTMLResponse)
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

    response = RedirectResponse('/items', status_code=status.HTTP_302_FOUND)
    return response

@router.get("/download", response_model=List[schemas.Item])
def download_items(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    # print(dir(items))
    item_list = model_list(items)
    print(item_list)

    file_content = str(item_list)
    basedir = os.path.abspath(os.path.dirname(__file__))
    print(basedir)
    print(basedir.find('demo_fastapi'), len('demo_fastapi'))
    rootPath = basedir[:basedir.find('demo_fastapi')+len('demo_fastapi')]
    print(rootPath)

    file_path = os.path.join(rootPath, 'temp', 'test.txt')
    print(file_path)
    with open(file_path, 'w') as f:
        f.write(file_content)
    return FileResponse(file_path, media_type='text/plain', filename='test.txt',background=BackgroundTask(lambda: os.remove(file_path)))


