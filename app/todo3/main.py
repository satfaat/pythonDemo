

from fastapi import FastAPI


app = FastAPI()
app.include_router(root.router)
app.include_router(api.router)
app.include_router(login.router)
app.include_router(reminders.router)


# @app.exception_handler(UnauthorizedPageException)
# async def unauthorized_exception_handler(request: Request, exc: UnauthorizedPageException):
#     return RedirectResponse('/login?unauthorized=True', status_code=302)


# @app.exception_handler(404)
# async def page_not_found_exception_handler(request: Request, exc: HTTPException):
#     if request.url.path.startswith('/api/'):
#         return JSONResponse({'detail': exc.detail}, status_code=exc.status_code)
#     else:
#         return RedirectResponse('/not-found')
