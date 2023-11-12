
## FastAPI

<details><summary>links</summary>

- [fastapi](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)
- [local docs](http://127.0.0.1:8000/docs)
- [localhost](http://127.0.0.1:8000/)
- [local redoc](http://127.0.0.1:8000/redoc)
- [tutorial](https://fastapi.tiangolo.com/tutorial/)
- [async](https://fastapi.tiangolo.com/async/#in-a-hurry)
- [](https://levelup.gitconnected.com/building-a-website-starter-with-fastapi-92d077092864)

</details>

### installation

```bash
pip install fastapi
pip install uvicorn[standard]
```

### run fastapi

```
uvicorn main:app --reload  # main.py app is object
uvicorn sql_app.main:app --reload
uvicorn app.main:app --reload --port 8080
```

- main: the file main.py (the Python "module").
- app: the object created inside of main.py with the line app = FastAPI().
- --reload: make the server restart after code changes. Only do this for development.

- [fast api host](http://127.0.0.1:8000)