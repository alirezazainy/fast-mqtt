from sqlalchemy.orm import Session
from .schemas import RequestBaseModel
from ..Models.models import Messages
from ..Models import crud
# Application controller layer

def get_all_messages(db: Session) -> list[Messages] | Messages | bool:
    """
    This function use database orm read function to try giving data from database

    Args:
        db (Session): database session with orm session type

    Returns:
        list[Messages] | Messages | bool: a list of messages or a message or boolean
    """
    try: # try connecting database and give data
        messages = crud.read(db)
        if not messages:# handling error
            not_error = False
        return messages
    except not_error:
        return not_error

def save_message(db:Session, request: RequestBaseModel) -> bool:
    """
    This function use database orm create function to try saving data to database

    Args:
        db (Session): database session with orm session type
        request (RequestBaseModel): request base model

    Returns:
        bool: result of saving data with True or False value
    """
    try:# try connecting database and save data
        result = crud.create(db, request)
        if not result:# handling error
            not_error = False
        return result
    except not_error:
        return not_error