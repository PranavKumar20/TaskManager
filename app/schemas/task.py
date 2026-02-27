from pydantic import BaseModel

#request Schema
class TaskCreate(BaseModel):
    title: str
    description: str
    is_completed: bool
    owner_id: int


#response Schema

class TaskResponse(BaseModel):
    id:int
    title: str
    description: str
    is_completed: bool
    owner_id: int

    class Config:
        from_attributes = True #instead of dict only it can read data from onject attribute like ORM model
