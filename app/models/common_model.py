"""Common model for all models."""
from datetime import datetime
from uuid import uuid4

from beanie import Document
from beanie.odm.fields import PydanticObjectId
from pydantic import BaseModel, Field


class CommonModel(Document, BaseModel):

    """Common model for all models."""

    id: PydanticObjectId = Field(default_factory=uuid4)
    enabled: bool = True
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    deleted_at: datetime | None = None

    async def save(self, *args, **kwargs):
        """Automatically set updated_at field on save."""
        self.updated_at = datetime.utcnow()
        await super().save(*args, **kwargs)
