from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    email: EmailStr


class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: Optional[bool] = False
    user_id: int