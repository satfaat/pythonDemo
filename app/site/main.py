from typing import Annotated
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer
from fastapi.staticfiles import StaticFiles
from app.site.configFastapi import templates
from src.features.web.reader import open_json, open_md

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

site = FastAPI(
    tags=['page']
)
site.mount('/static', StaticFiles(directory='site/front/static'), name='static')


@site.get("/")
def home(request: Request):
    data = {
        'page': 'index',
        'md_content': open_md('home.md', "site/front/pages/")}
    context = {
        "request": request,
        "data": data}
    return templates.TemplateResponse("site/index.html", context)


@site.get("/md/", response_class=HTMLResponse)
async def index(request: Request):
    data = {
        'page': 'index',
        'md_content': open_md('home.md', "site/front/pages/")}
    return templates.TemplateResponse('site/index.html',
                                      {'request': request, 'data': data})


@site.get("/md/{page_name}")
async def page(request: Request, page_name: str):
    data = {
        "page": page_name,
        'md_content': open_md(f'{page_name}.md', "site/front/pages/")}
    return templates.TemplateResponse('site/index.html',
                                      {'request': request, 'data': data})


@site.get("/form/", response_class=HTMLResponse)
async def formDemo(request: Request):
    return templates.TemplateResponse("forms/formDemo.html", {"request": request})


@site.get("/about")
def about(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("site/about.html", context)


@site.get("/contact")
def contact(request: Request):
    context = {
        "request": request,
        "title": "Contact"}
    return templates.TemplateResponse("site/contact.html", context)


@site.get("/api/public")
def public():
    """No access token required to access this route"""

    result = {
        "status": "success",
        "msg": ("Hello from a public endpoint! You don't need to be "
                "authenticated to see this.")
    }
    return result


@site.get("/api/private")
def private(token: Annotated[str, Depends(oauth2_scheme)]):
    """A valid access token is required to access this route"""

    result = {"token": token}

    return result
