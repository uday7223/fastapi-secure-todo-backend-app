from pydantic import BaseModel, Field, EmailStr, validator
from datetime import date



#this is for todos
class TodoIn(BaseModel):
    title: str = Field(..., min_length=5, max_length=50)
    date: date

    @validator("date")
    def validate_due_date(cls, v):
        if v < date.today():
            raise ValueError("Due date cannot be in the past")
        return v

class TodoOut(TodoIn):
    id: int
    completed: bool

    class Config:
        orm_mode = True

# this is for user registration
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
