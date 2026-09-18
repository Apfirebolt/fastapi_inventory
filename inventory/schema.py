from datetime import datetime
from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    title: str = Field(..., max_length=255)
    quantity: int = Field(..., ge=0)


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    title: str | None = Field(None, max_length=255)
    quantity: int | None = Field(None, ge=0)


class ItemResponse(ItemBase):
    id: int
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True