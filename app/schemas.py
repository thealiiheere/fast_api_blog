from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional
from datetime import datetime

class PostCreate(BaseModel):
    title: str
    body: str
    published: bool = True
    rating: Optional[int] = None    # ← YANGI

class PostUpdate(BaseModel):
    title: str
    body: str
    published: bool
    


class PostResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    body: str
    published: bool
    created_at: datetime
    owner_id: Optional[int] = None


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr
    created_at: datetime

# ─── TOKEN SCHEMAS ────────────────────────────

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None


