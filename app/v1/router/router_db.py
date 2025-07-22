from fastapi import APIRouter
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: str | None = Field(default=None, index=True)
    complete: bool = Field(index=True)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"


connect
