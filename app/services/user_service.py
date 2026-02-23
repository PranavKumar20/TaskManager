from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from fastapi import HTTPException

def create_user(db: Session, user_data: UserCreate):
    user = User(
        name = user_data.name,
        email = user_data.email,
        password = user_data.password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_user_by_id(db: Session, user_id: int):
    return db.get(User, user_id)

def get_all_users(db: Session):
    return db.query(User).all()

def delete_user_by_id(db: Session, user_id: int):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return "user data deleted successfully"

def update_user_by_id(db: Session, user_id: int, user_data):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found for the provided user_id")
    user.name = user_data.name
    user.email = user_data.email
    user.password = user_data.password
    db.commit()
    db.refresh(user)
    return user