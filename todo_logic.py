# todo_logic.py

todos = [
    {
        "id": 1,
        "title": "Buy groceries",
        "date": "2023-10-01",
        "completed": False
    },
    {
        "id": 2,
        "title": "Walk the dog",
        "date": "2023-10-02",
        "completed": False
    },
    {
        "id": 3,
        "title": "Read a book",
        "date": "2023-10-03",
        "completed": True
    }
 ]

def add_task(title, date):
    task = {
        "id": len(todos) + 1,
        "title": title,
        "date": date,
        "completed": False
    }
    todos.append(task)
    return task

def list_tasks():
    print("Listing all tasks:")
    for task in todos:
        print(f"Task ID: {task['id']}, Title: {task['title']}, Date: {task['date']}, Completed: {task['completed']}")
    return todos

def mark_done(task_id: int):
    for task in todos:
        if task["id"] == task_id:
            task["completed"] = True
            return task
    return None

def delete_task(task_id: int):
    global todos
    for task in todos:
        if task["id"] == task_id:
            todos = [t for t in todos if t["id"] != task_id]
            return {"message": "Task deleted"}
    return {"error": "Task not found"}
