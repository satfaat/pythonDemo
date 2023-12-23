
import uuid
import app.todo2.back.crud as crud
from fastapi import Depends, FastAPI, Form, HTTPException, Query, Request, Response
from fastapi.responses import HTMLResponse
from sqlmodel import Session
from app.features.database import get_session
from app.todo2.configFastapi import templates


todo = FastAPI()


@todo.get("/", response_class=HTMLResponse)
async def home(req: Request,
               session: Session = Depends(get_session),
               skip: int = 0,
               limit: int = Query(default=100, le=100),):
    session_key = req.cookies.get("session_key", uuid.uuid4().hex)
    todos = crud.get_all(session,
                         session_key,
                         skip,
                         limit)
    context = {
        "request": req,
        "todos": todos,
        "title": "Home"
    }
    res = templates.TemplateResponse("todo/home.html", context)
    res.set_cookie(key="session_key",
                   value=session_key,
                   expires=259200)  # 3 days
    return res


@todo.get("/edit/{todo_id}", response_class=HTMLResponse)
async def get_edit_record(req: Request,
                          todo_id: int,
                          session: Session = Depends(get_session)):
    todo = crud.get_by_id(session, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Task not found")
    context = {"request": req, "todo": todo}
    return templates.TemplateResponse("todo/form.html", context)


@todo.post("/add", response_class=HTMLResponse)
def post_add(req: Request,
             task: str = Form(...),
             session: Session = Depends(get_session)):
    session_key = req.cookies.get("session_key")
    todo = crud.create(session,
                       task,
                       session_key)
    context = {"request": req, "todo": todo}
    return templates.TemplateResponse("todo/item.html", context)


@todo.put("/edit/{todo_id}", response_class=HTMLResponse)
def put_edit(req: Request,
             todo_id: int,
             task: str = Form(...),
             session: Session = Depends(get_session)):
    todo = crud.update_by_id(session,
                             todo_id,
                             task)
    context = {"request": req, "todo": todo}
    return templates.TemplateResponse("todo/item.html", context)


@todo.delete("/delete/{todo_id}", response_class=Response)
def delete(todo_id: int,
           session: Session = Depends(get_session)):
    crud.delete_by_id(session, todo_id)
