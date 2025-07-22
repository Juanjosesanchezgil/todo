from typing import Annotated
from fastapi import Depends, APIRouter
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: str | None = Field(default=None, index=True)
    complete: bool = Field(index=True)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"


connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


router = APIRouter(prefix="/tasks", tags=["task_db"])


@router.get("/")
def get_tasks(session: SessionDep) -> list[Task]:
    tasks = session.exec(select(Task)).all()
    return tasks


@router.post("/")
def create_task(task: Task, session: SessionDep) -> Task:
    session.add(task)
    session.commit()
    session.refresh(task)
    return task
