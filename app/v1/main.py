from fastapi import FastAPI
from app.v1.router.router_list import router as tasks_router


app = FastAPI()

app.include_router(tasks_router)


@app.get("/")
def hello_world():
    return {"msg": "Hello world"}
