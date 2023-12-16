
from fastapi.responses import RedirectResponse
import app.todo.crud as crud
from typing import List
from fastapi import Depends, FastAPI, Form, HTTPException, Query, Request, status
from sqlmodel import Session, select
from configs.configFastapi import templates
from app.features.database import get_session
from app.todo.models import Todo

todo = FastAPI()
# todo = APIRouter(
#     prefix='/api/todo',
#     tags=["todo"]
# )


@todo.get("/", response_model=List[Todo])
async def todo_records(req: Request,
                       session: Session = Depends(get_session),
                       skip: int = 0,
                       limit: int = Query(default=100, le=100),):
    todos = crud.get_all(session, skip, limit)
    return templates.TemplateResponse("index.html", {"request": req, "todos": todos})


@todo.get("/edit/{todo_id}", response_model=Todo)
async def todo_record(req: Request,
                      todo_id: int,
                      session: Session = Depends(get_session)):
    todo = crud.get_by_id(session, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Task not found")
    return templates.TemplateResponse("todo/edit.html", {"request": req, "todo": todo})


@todo.post("/add")
async def add(task: str = Form(...),
              is_complete: bool = Form(False),
              session: Session = Depends(get_session)):
    todo = Todo(task=task, is_complete=is_complete)
    session.add(todo)
    session.commit()
    return RedirectResponse('http://127.0.0.1:8000/api/todo/', status.HTTP_303_SEE_OTHER)


@todo.post("/edit/{todo_id}")
async def add(todo_id: int,
              task: str = Form(...),
              is_complete: bool = Form(False),
              session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    todo.task = task
    todo.is_complete = is_complete
    session.commit()
    return RedirectResponse('http://127.0.0.1:8000/api/todo/', status.HTTP_303_SEE_OTHER)


@todo.get("/delete/{todo_id}")
async def delete_task(todo_id: int,
                      session: Session = Depends(get_session)):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(404, "Task not found")
    session.delete(todo)
    session.commit()
    return RedirectResponse('http://127.0.0.1:8000/api/todo/',
                            status.HTTP_303_SEE_OTHER)
