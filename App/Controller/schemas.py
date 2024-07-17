from pydantic import BaseModel
# Controller schemas library

#TODO: generate new classes for base models of req and res and new models for other jobs
class RequestBaseModel(BaseModel):
    """
    This class sets request rules for fastapi requesting system
    inherits from pydantic base model
    """
    id : int
    imei: str
    micro_op: str
    class Config:
        orm_mode = True
    
class ResponseModel(BaseModel):
    """
    This class sets response rules for fastapi responding system
    inherits from pydantic base model
    """
    imei: str
    micro_op: str

    class Config:
        orm_mode = True
    