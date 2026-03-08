from pydantic import BaseModel
from typing import Optional

class UserIn(BaseModel):
    name: str
    email: str
    password: str

class UserOut(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        from_attributes = True

class AuthResponse(BaseModel):
    user: UserResponse
    token: str