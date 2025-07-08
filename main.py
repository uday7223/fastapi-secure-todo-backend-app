from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import utils, auth
from database import SessionLocal, engine
from deps import get_db
from oauth2 import get_current_user
from todo_logic import add_task, list_tasks, mark_done, delete_task
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import models
import schemas

models.Base.metadata.create_all(bind=engine)


app = FastAPI()



origins = [
    "https://taskify-app-wpmp.onrender.com",  # your frontend domain
    "http://localhost:5173",  # local dev, optional
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # or ["*"] to allow all (not safe for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/todos", response_model=list[schemas.TodoOut])
def get_all_todos(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    print("Current User:", current_user)  # Debugging line
    return db.query(models.Todo).filter(models.Todo.user_id == current_user.id).all()

@app.post("/todos", response_model=schemas.TodoOut, status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.TodoIn, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    new_task = models.Todo(**todo.dict(), user_id=current_user.id)  # 👈 link todo to logged-in user
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.put("/todos/{task_id}", response_model=schemas.TodoOut)
def mark_complete(task_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    task = db.query(models.Todo).filter(models.Todo.id == task_id, models.Todo.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found or not authorized")
    if task.completed == True:
        task.completed = False
    else:
        task.completed = True
    db.commit()
    db.refresh(task)
    return task

@app.delete("/todos/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    task = db.query(models.Todo).filter(models.Todo.id == task_id,  models.Todo.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found or not authorized")
    db.delete(task)
    db.commit()
    return {
    "message": "Task deleted",
    "task_details": {
        "id": task.id,
        "title": task.title,
        "date": task.date,
        "completed": task.completed
    }
}

@app.post("/register", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered !!")
    
    hashed_pwd = utils.hash_password(user.password)
    new_user = models.User(username=user.username, email=user.email, hashed_password=hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not utils.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    access_token = auth.create_access_token(data={"id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
