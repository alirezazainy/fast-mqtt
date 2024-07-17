from sqlalchemy.orm import Session
from .models import Messages
from ..Controller.schemas import RequestBaseModel
# CRUD ORM functions

def create(db: Session, request: RequestBaseModel) -> bool:
    """
    This function saves data to database

    Args:
        db (Session): database session with orm session type
        request (RequestBaseModel): request base model 

    Returns:
        bool: return true if completely finished
    """
    message = Messages(
        imei=request.imei,
        micro_op=request.micro_op
    ) # -> add instance
    # add instance to database
    db.add(message)
    db.commit()
    db.refresh(message)
    return True

def read(db: Session, request: RequestBaseModel | None = None) -> list[Messages] | Messages:
    """
    This function read items from database 
    
    if you give a request model, the function searches in the database for a list of messages you give the imei or micro operation
        or give a message with ID

    Args:
        db (Session): database session with orm session type
        request (RequestBaseModel | None, optional): request base model. Defaults to None.

    Returns:
        list[Messages] | Messages: return a list of messages or a message
    """
    if request is not None:
        if request.id is not None:
            # search in ids
            return db.query(Messages).filter(Messages.ID == request.id).first()
        else:
            # search in imeis and micro ops 
            return db.query(Messages).filter(Messages.imei == request.imei or Messages.micro_op == request.micro_op).order_by(Messages.time_stamp).all()
    else:
        # get all of the database messages
        return db.query(Messages).all()

