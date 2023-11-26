from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles
from fastapiDem.src.routers.page import router as page
from fastapiDem.src.routers.posts import router as posts
from fastapiDem.src.routers.users import router as users


app = FastAPI()
app.mount('/static', StaticFiles(directory='./static'), name='static')


@app.get("/info")
def info() -> str:
    return f"about fast api: {type(app)}"


app.include_router(page)
app.include_router(posts)
app.include_router(users)
