from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/tasks", tags=["tasks"])


class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    complete: bool


tasks_list = [
    Task(id=1, title="tarea 1", description="decripcion 1", complete=True),
    Task(id=2, title="tarea 2", complete=False)
]


@router.get("/")
async def get_tasks():
    return tasks_list
