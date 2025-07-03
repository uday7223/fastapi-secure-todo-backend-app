from sqlalchemy import Column, Integer, String, Boolean,  Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    completed = Column(Boolean, default=False)
    
    # 🔐 Associate with user
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="todos")

#user model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    # Inside User class
    todos = relationship("Todo", back_populates="owner")

