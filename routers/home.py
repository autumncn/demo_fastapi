import datetime
import time

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db import schemas, crud
from db.database import get_db
from dependencies import templates
from logs.logger import logger

router = APIRouter()

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("general_pages/homepage.html",{"request":request})
