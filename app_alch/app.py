from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from sqlmodel import Session, select
from app_alch.modelSql.Todo import Todo
from routers.heroes import router as heroes
from routers.team import router as team
from configs.configDB import engine
from configs.configFastapi import templates
from app_alch.features.database import create_db_and_tables
from contextlib import asynccontextmanager


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     create_db_and_tables()

app = FastAPI()
app.mount('/static', StaticFiles(directory='../static'), name='static')


app.include_router(heroes)
app.include_router(team)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def todo_records(req: Request):
    with Session(engine) as session:
        todos = session.exec(select(Todo)).all()
        return templates.TemplateResponse("base.html", {"request": req, "todo_list": todos})
