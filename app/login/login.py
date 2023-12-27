

from typing import Optional
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from app.login.configFastapi import templates


login = FastAPI(
    default_response_class=HTMLResponse
)


@login.get("/login",
           summary="Gets the login page",
           tags=["Pages", "Authentication"],
           response_class=HTMLResponse)
async def get_login(request: Request,
                    invalid: Optional[bool] = None,
                    logged_out: Optional[bool] = None,
                    unauthorized: Optional[bool] = None):

    context = {'request': request,
               'invalid': invalid,
               'logged_out': logged_out,
               'unauthorized': unauthorized}
    return templates.TemplateResponse("pages/login.html", context)


@login.post(path="/login",
            summary="Logs into the app",
            tags=["Authentication"])
async def post_login(cookie: Optional[AuthCookie] = Depends(get_login_form_creds)) -> dict:

    if not cookie:
        return RedirectResponse('/login?invalid=True', status_code=302)
    response = RedirectResponse('/reminders', status_code=302)
    response.set_cookie(key=cookie.name, value=cookie.token)

    return response


logout = dict(
    path="/logout",
    summary="Logs out of the app",
    tags=["Authentication"]
)


@login.get(**logout)
@login.post(**logout)
async def post_login(cookie: Optional[AuthCookie] = Depends(get_auth_cookie)) -> dict:
    if not cookie:
        raise UnauthorizedPageException()

    response = RedirectResponse('/login?logged_out=True', status_code=302)
    response.set_cookie(key=cookie.name, value=cookie.token, expires=-1)
    return response
