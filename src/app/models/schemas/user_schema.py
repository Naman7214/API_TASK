from pydantic import BaseModel, EmailStr
from typing import Literal

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Literal["admin", "buyer", "seller"]

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserRoleUpdate(BaseModel):
    role: Literal["admin", "buyer", "seller"]

class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None

class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
