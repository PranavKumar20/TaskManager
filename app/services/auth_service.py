from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth import LoginRequest, Token
from fastapi import HTTPException
import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "SECRET_KEY_TOO_SECRET_CAN'T_BE_GUESSED"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 7200


#function 1: function to handle signin -> dividing for easy cleanliness -> filter for user, check present or not
# now its time ti verify password, lets create another function, no necessary though
# now time to generate JWT token, better to create another function, pass only the required data to keep all functions clean


def handle_signin(db: Session, login_data: LoginRequest):
    user = db.query(User).filter(User.email == login_data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User no found")
    if not verify_password(user, login_data):
        raise HTTPException(status_code=401, detail="Wrong Credentials")
    return create_access_token(login_data.email, ACCESS_TOKEN_EXPIRE_MINUTES)



def verify_password(user: User, to_check_data: LoginRequest):
    if user.password == to_check_data.password:
        return True
    return False
        

def create_access_token(data: str, expires_delta: timedelta):
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode = {
        "sub":data,
        "exp":expire
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt 