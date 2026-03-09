from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth import LoginRequest, Token
from fastapi import HTTPException
import jwt
from datetime import datetime, timedelta, timezone
from app.core.config import settings


#function 1: function to handle signin -> dividing for easy cleanliness -> filter for user, check present or not
# now its time ti verify password, lets create another function, no necessary though
# now time to generate JWT token, better to create another function, pass only the required data to keep all functions clean


def handle_signin(db: Session, login_data: LoginRequest):
    user = db.query(User).filter(User.email == login_data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User no found")
    if not verify_password(user, login_data):
        raise HTTPException(status_code=401, detail="Wrong Credentials")
    return create_access_token(login_data.email, settings.ACCESS_TOKEN_EXPIRE_MINUTES)


# later we will use password hashing, hence will will compare hashes 
def verify_password(user: User, to_check_data: LoginRequest):
    if user.password == to_check_data.password:
        return True
    return False
        

def create_access_token(data: str, expires_delta: int):
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
    to_encode = {
        "sub":data,
        "exp":expire
    }
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return {"access_token":encoded_jwt }