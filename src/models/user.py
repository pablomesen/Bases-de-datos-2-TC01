from pydantic import BaseModel, EmailStr
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    READER = "reader"

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.READER

class User(UserBase):
    id: int
    role: UserRole

    class Config:
        orm_mode = True
