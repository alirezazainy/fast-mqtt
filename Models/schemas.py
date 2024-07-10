from pydantic import BaseModel
#TODO: generate new classes for base models of req and res and new models for other jobs
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
    method: str
    class Config:
        orm_mode = True
    