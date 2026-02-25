from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate
from fastapi import HTTPException


def create_task(db: Session,task: TaskCreate):
    task = Task(
        title = task.title,
        description = task.description,
        is_complete = task.is_completed,
        owner_id = task.owner_id
    )
    db.add(task)
    db.commit()
    db.refresh()

    return task

def get_all_task(db: Session):
    tasks = db.query(Task).all()
    return tasks

def get_task_by_id(task_id: int, db: Session):
    task = db.get(Task, task_id)
    return task

def delete_task_by_id(task_id: int, db: Session):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return "Task data deleted successfully"

def update_task_by_id(task_id: int, task_data: TaskCreate, db: Session):
    task = db.get(Task, task_id)
    task.title = task_data.title
    task.description = task_data.description
    task.is_completed = task_data.is_completed
    task.owner_id = task_data.owner_id
    db.commit()
    db.refresh()
    return task

def get_tasks_by_user_id(user_id: int, db: Session):
    tasks = db.query(Task).filter(Task.user_id == user_id).all()
    return tasks