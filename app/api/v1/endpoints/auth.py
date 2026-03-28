from fastapi import APIRouter, Depends
from app.schemas.auth import LoginRequest, Token, SigninResponse
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.services.auth_service import handle_signin

router = APIRouter()

@router.post("/signin", response_model=SigninResponse)
def signin(
    login_data: LoginRequest,
    db: Session = Depends(get_db) 
):
    return handle_signin(db, login_data)

