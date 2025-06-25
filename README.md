# 📝 FastAPI Todo App with JWT Authentication

A secure full-stack Todo application backend built with **FastAPI**, **PostgreSQL**, and **JWT Authentication**.

## 🚀 Features

- 🔐 User **Registration & Login** using JWT
- ✅ Fully functional **CRUD** operations on todos
- 👤 Todos are linked to authenticated users only
- ⚙️ Database powered by **PostgreSQL** with SQLAlchemy ORM
- 📄 Auto-generated API docs with **Swagger UI**
- 🧪 Tested using **Postman**

## 🛠️ Tech Stack

- **Backend Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT (OAuth2PasswordBearer)
- **Schema Validation**: Pydantic
- **API Testing**: Postman

---

## 📁 Project Structure

fastapi-todo/
├── main.py
├── models.py
├── schemas.py
├── database.py
├── auth.py
├── oauth2.py
└── requirements.txt


---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/fastapi-todo.git
cd fastapi-todo

Create Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

Install Dependencies
pip install -r requirements.txt

Configure Database
Update your PostgreSQL connection URL inside database.py:
DATABASE_URL = "postgresql://<username>:<password>@localhost:5432/todo_db"

Run the Server
uvicorn main:app --reload

🔑 API Authentication (JWT)
Get token from /login

Use token in Authorization Header as: Bearer <your-access-token>

📬 API Endpoints
| Method | Endpoint      | Description           |
| ------ | ------------- | --------------------- |
| POST   | `/register`   | Register new user     |
| POST   | `/login`      | Login and get token   |
| GET    | `/todos`      | Get all user todos    |
| POST   | `/todos`      | Create a new todo     |
| PUT    | `/todos/{id}` | Mark todo as complete |
| DELETE | `/todos/{id}` | Delete a todo         |


🧪 API Testing with Postman
Register/Login to get the JWT token

Add token in Authorization → Bearer Token

Perform CRUD on /todos endpoints

📸 Swagger UI
Interactive API docs available at:
http://127.0.0.1:8000/docs

✅ Next Improvements
⏳ Pagination

🔎 Search & filter todos

🐳 Dockerize the project

🌐 Build frontend with React.js



🙌 Acknowledgments
Built with 💙 using FastAPI.
Inspired by real-world project needs to help master Python for backend development.

📌 Author
Udaykumar N
GitHub :  https://github.com/uday7223

📌 Note
This was a practice backend project to master Python for backend development before working on the main internship assignment.

