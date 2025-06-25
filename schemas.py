from pydantic import BaseModel, Field, EmailStr


#this is for todos
class TodoIn(BaseModel):
    title: str = Field(..., min_length=5, max_length=50)
    date: str

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
