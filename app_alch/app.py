from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from sqlmodel import Session, select
from routers.heroes import router as heroes
from routers.team import router as team
from configs.configDB import engine
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
