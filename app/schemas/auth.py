from pydantic import BaseModel, EmailStr

#login resquest
class LoginRequest(BaseModel):
    email: EmailStr
    password: str


#login response
class Token(BaseModel):
    access_token: str
    token_type: str = 'Bearer'

class SigninResponse(BaseModel):
    access_token: str
    token_type: str = 'Bearer'
    user_id: int
    user_name: str