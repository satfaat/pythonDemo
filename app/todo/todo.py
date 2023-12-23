

from fastapi import FastAPI
from app.todo.back.router import todo as todo_api


todo = FastAPI()

todo.include_router(todo_api)
