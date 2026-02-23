from pydantic import BaseModel

#common response schema(need message)
class MessageResponse(BaseModel):
    message: str

