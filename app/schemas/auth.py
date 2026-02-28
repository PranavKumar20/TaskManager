from pydantic import BaseModel, EmailStr

#login resquest
class LoginRequest(BaseModel):
    email: EmailStr
    password: str


#login response
class Token(BaseModel):
    access_token: str
    token_type: str = 'Bearer'