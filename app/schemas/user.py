from pydantic import BaseModel, EmailStr

#request schema
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

#response schema
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class config:
        from_attributes = True

