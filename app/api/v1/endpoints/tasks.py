from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.task import TaskCreate, TaskResponse
from app.schemas.common import MessageResponse
from app.services.task_service import create_task, get_all_task, get_task_by_id, delete_task_by_id, update_task_by_id


router = APIRouter()

# route to create task -> input: TaskCreate -> output: TaskResponse
@router.post("/", response_model=TaskResponse)
def create_new_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    return create_task(db,task)

#route to get all tasks -> input: nothing -> output: list of Taskresponse
@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db)
):
    return get_all_task(db)

#route to get task by id -> input: task_is -> output: task related to that id
@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    return get_task_by_id(task_id, db)

#route to delete task by id -> input: task_id -> output: a msg stating the deletion of task
@router.delete("/{task_id}", response_model=MessageResponse)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    return delete_task_by_id(task_id, db)

#route to update task by id -> input: task_id as path parameter, inputs as body parameter -> output: return updated task
@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_data: TaskCreate,
    db: Session = Depends(get_db)
):
    return update_task_by_id(task_id, task_data,db)

#route to fetch tasks created by a user -> input: user_id -> output: list of tasks created by user
@router.get("/{user_id}", response_model=list[TaskResponse])
def get_user_tasks(
    user_id: int,
    db: Session = Depends(get_db)
):
    return 
