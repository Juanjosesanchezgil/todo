from fastapi import APIRouter
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    