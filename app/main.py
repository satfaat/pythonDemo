from fastapi.responses import HTMLResponse
import app.site.back.menu.crudTinybd as read_menu
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from app.heroes.heroes import heroes
from app.todo.todo import todo
from app.todo2.todo import todo as todo2
from app.demo.demo import demo
from app.features.database import create_db_and_tables
from contextlib import asynccontextmanager
from src.features.web.reader import open_md
from configs.configFastapi import templates
# from configs.oth.adminConf import amis_admin


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     create_db_and_tables()

app = FastAPI()
app.mount('/static', StaticFiles(directory='../front/static'), name='static')
app.mount('/demo', demo)
app.mount('/todo', todo)
app.mount('/todo2', todo2)
app.mount('/heroes', heroes)


@app.on_event("startup")
def on_startup() -> None:
    create_db_and_tables()


# amis_admin.mount_app(app)


@app.get("/")
def home(request: Request):
    menu = read_menu.get_all_records()
    data = {
        'page': 'index',
        'md_content': open_md('home.md', "../front/pages/")}
    context = {
        "request": request,
        "data": data,
        "menu": menu}
    return templates.TemplateResponse("site/index.html", context)


@app.get("/md/", response_class=HTMLResponse)
async def index(request: Request):
    data = {
        'page': 'index',
        'md_content': open_md('home.md', "../front/pages/")}
    return templates.TemplateResponse('site/index.html',
                                      {'request': request, 'data': data})


@app.get("/md/{page_name}")
async def page(request: Request, page_name: str):
    data = {
        "page": page_name,
        'md_content': open_md(f'{page_name}.md', "../front/pages/")}
    return templates.TemplateResponse('site/index.html',
                                      {'request': request, 'data': data})


@app.get("/form/", response_class=HTMLResponse)
async def formDemo(request: Request):
    return templates.TemplateResponse("forms/formDemo.html", {"request": request})


@app.get("/about")
def about(request: Request):
    menu = read_menu.get_all_records()
    context = {
        "request": request,
        "menu": menu}
    return templates.TemplateResponse("site/about.html", context)


@app.get("/contact")
def contact(request: Request):
    menu = read_menu.get_all_records()
    context = {
        "request": request,
        "menu": menu}
    return templates.TemplateResponse("site/contact.html", context)


@app.get("/blog")
def blog(request: Request):
    menu = read_menu.get_all_records()
    context = {
        "request": request,
        "menu": menu}
    return templates.TemplateResponse("site/blog.html", context)
