
from fastapi import APIRouter, Depends
import app_alch.schemas.item as itemSchema
import app_alch.crud.crud as crud
from sqlalchemy.orm import Session
from configs.dbConf.sqlAlch import get_db


router = APIRouter()


@router.get("/items/", response_model=list[itemSchema.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
