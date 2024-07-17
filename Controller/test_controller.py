from sqlalchemy.orm import Session
from Controller.schemas import RequestBaseModel
from Models import crud

def get_all_messages(db: Session):
    try:
        messages = crud.read(db)
        if not messages:
            error = True
        return messages
    except error:
        return error

def save_message(db:Session, request: RequestBaseModel):
    try:
        result = crud.create(db, request)
        if not result:
            error = True
        return result
    except error:
        return error