from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapiDem.configs.config import templates
from fastapiDem.src.features.reader import open_json, open_md


router = APIRouter(
    tags=['page']
)


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    data_htm = {
        'template_name': 'index.html',
        'title': 'Home page',
        'page': 'index',
        'md_content': open_md('home.md')
    }
    return templates.TemplateResponse(
        data_htm['template_name'],
        {'request': request, 'data': data_htm}
    )


@router.get("/page/{page_name}")
async def page(request: Request, page_name: str):
    data = {
        'template_name': 'index.html',
        "page": page_name,
        'md_content': open_md(page_name+'.md')
    }
    return templates.TemplateResponse(
        data['template_name'],
        {'request': request, 'data': data}
    )


@router.get("/form/", response_class=HTMLResponse)
async def formDemo(request: Request):
    return templates.TemplateResponse("formDemo.html", {"request": request})
