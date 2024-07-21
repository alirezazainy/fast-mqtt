from pydantic import BaseModel

# Controller schemas library


class MessageBaseModel(BaseModel):
    """
    This class sets request and response rules for fastapi requesting system
    inherits from pydantic base model
    """

    imei: str
    micro_op: str

    class Config:
        from_attributes = True
