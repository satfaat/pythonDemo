from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.heroes.heroes import heroes
from app.todo.todo import todo
from app.features.database import create_db_and_tables
from contextlib import asynccontextmanager
# from configs.oth.adminConf import amis_admin


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     create_db_and_tables()

app = FastAPI()
app.mount('/static', StaticFiles(directory='../static'), name='static')
app.mount('/api/todo', todo)
app.mount('/api/heroes', heroes)


@app.on_event("startup")
def on_startup() -> None:
    create_db_and_tables()


# amis_admin.mount_app(app)
