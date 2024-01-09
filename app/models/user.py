"""User model."""

from uuid import UUID

from beanie import Document
from pydantic import BaseModel

from .common_model import CommonModel


class User(CommonModel, Document):

    """User model."""

    first_name: str
    last_name: str | None = None
    patronymic: str | None = None


class UserCreate(BaseModel):

    """User create model."""

    email: str
    first_name: str
    last_name: str | None = None
    patronymic: str | None = None
    password: str


class UserUpdate(BaseModel):

    """User update model."""

    uuid: UUID
    email: str
    first_name: str
    last_name: str | None = None
    patronymic: str | None = None
    password: str
