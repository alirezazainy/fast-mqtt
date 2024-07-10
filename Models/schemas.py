from pydantic import BaseModel

class RequestModel(BaseModel):
    """
    This class sets request rules for fastapi requesting system
    inherits from pydantic base model
    """
    message: str
    class Config:
        orm_mode = True
    
class ResponseModel(BaseModel):
    """
    This class sets response rules for fastapi responding system
    inherits from pydantic base model
    """
    topic: str
    message: str
    status_code: int
    class Config:
        orm_mode = True
    