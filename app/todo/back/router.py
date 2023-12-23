
import app.todo.back.crud as crud
from typing import List
from fastapi import Depends, APIRouter, Form, HTTPException, Query, Request, status
from fastapi.responses import RedirectResponse
from sqlmodel import Session
from configs.configFastapi import templates
from app.features.database import get_session
from app.todo.back.models import Todo


todo = APIRouter(
    prefix='',
    tags=['todo']
)


@todo.get("/", response_model=List[Todo])
async def todo_records(req: Request,
                       session: Session = Depends(get_session),
                       skip: int = 0,
                       limit: int = Query(default=100, le=100),):
    todos = crud.get_all(session, skip, limit)
    return templates.TemplateResponse("index.html", {"request": req, "todos": todos})


@todo.get("/edit/{todo_id}", response_model=Todo)
# .put
async def todo_record(req: Request,
                      todo_id: int,
                      session: Session = Depends(get_session)):
    todo = crud.get_by_id(session, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Task not found")
    # todo.task = task
    # session.commit()
    return templates.TemplateResponse("todo/edit.html", {"request": req, "todo": todo})


@todo.post("/edit/{todo_id}")
async def add(todo_id: int,
              task: str = Form(...),
              is_complete: bool = Form(False),
              session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    todo.task = task
    todo.is_complete = is_complete
    session.commit()
    return RedirectResponse('/todo/', status.HTTP_303_SEE_OTHER)


@todo.post("/add", status_code=status.HTTP_201_CREATED)
async def add(task: str = Form(...),
              is_complete: bool = Form(False),
              session: Session = Depends(get_session)):
    todo = Todo(task=task, is_complete=is_complete)
    session.add(todo)
    session.commit()
    return RedirectResponse('/todo/', status.HTTP_303_SEE_OTHER)


@todo.put("/{id}")
def update_todo(id: int):
    return "update todo item with id {id}"


@todo.delete("/{id}")
def delete_todo(id: int):
    return "delete todo item with id {id}"


@todo.get("/delete/{todo_id}")
async def delete_task(todo_id: int,
                      session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(404, "Task not found")
    session.delete(todo)
    session.commit()
    return RedirectResponse('/todo/',
                            status.HTTP_303_SEE_OTHER)
