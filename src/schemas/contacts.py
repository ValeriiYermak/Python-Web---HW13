from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, EmailStr

from src.schemas.user import UserResponse


class ContactSchema(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    lastname: str = Field(min_length=3, max_length=50)
    email: EmailStr
    phone: str = Field(min_length=7, max_length=50)
    birthdate: str = Field(min_length=7, max_length=50)
    others_info: str = Field(min_length=5, max_length=250)
    completed: Optional[bool] = False


class ContactUpdateSchema(ContactSchema):
    completed: bool


class ContactResponse(BaseModel):
    id: int = 1
    name: str
    lastname: str
    email: EmailStr
    phone: str
    birthdate: str
    others_info: str
    completed: bool
    created_at: datetime | None
    updated_at: datetime | None
    user: UserResponse | None

    class Config:
        from_attributes = True
