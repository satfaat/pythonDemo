

from typing import List
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlmodel import Session, select
from app_alch.features.database import get_session
from configs.configFastapi import templates
from app_alch.modelSql.Todo import Todo


router = APIRouter(
    prefix='/api',
    tags=["todo"]
)


@router.get("/todo/", response_model=List[Todo])
async def todo_records(req: Request, session: Session = Depends(get_session)):
    todos = session.exec(select(Todo)).all()
    return templates.TemplateResponse("base.html", {"request": req, "todo_list": todos})


@router.get("/edit/{todo_id}", response_model=Todo)
async def todo_record(req: Request, todo_id: int, session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Task not found")
    return templates.TemplateResponse("edit.html", {"request": req, "todo": todo})
