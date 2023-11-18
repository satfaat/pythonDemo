from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles
from fastapiDem.src.routers.page import router as page_router
from fastapiDem.src.routers.posts import router as posts_router
from fastapiDem.src.routers.users import router as users_router


app = FastAPI()
app.mount('/static', StaticFiles(directory='./static'), name='static')


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


app.include_router(page_router,
                   tags=["page"])
app.include_router(posts_router, prefix="/posts",
                   tags=["posts"])
app.include_router(users_router, prefix="/users",
                   tags=["users"])
