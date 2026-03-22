from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.schemas.user import UserCreate, UserResponse
from app.schemas.common import MessageResponse
from app.services.user_service import create_user, get_user_by_id, get_all_users, delete_user_by_id, update_user_by_id
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)

@router.get("/", response_model=list[UserResponse])
async def get_users(
    db: Session = Depends(get_db)
):
    return get_all_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_user_by_id(db, user_id)

# @router.delete("/{user_id}", response_model=MessageResponse)
# def delete_user(
#     user_id: int,
#     db: Session = Depends(get_db)
# ):
#     msg = delete_user_by_id(db, user_id)
#     return {"message": msg}

@router.delete("/{user_id}", response_model=MessageResponse)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user:User = Depends(get_current_user)
):
    msg = delete_user_by_id(db, user_id, current_user)
    return {"message": msg}

@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user:User = Depends(get_current_user)
):
    return update_user_by_id(db, user_id, user,current_user)
    