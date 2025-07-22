from fastapi import FastAPI
from router.router_db import create_db_and_tables, router as tasks_router


app = FastAPI()

app.include_router(tasks_router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
def hello_world():
    return {"msg": "Hello world"}
