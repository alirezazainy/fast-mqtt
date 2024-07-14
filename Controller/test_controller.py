from sqlalchemy.orm import Session
from schemas import RequestBaseModel
from ..Models import crud

def get_all_messages(db: Session):
    try:
        messages = crud.read(db)
        if not messages:
            error = True
        yield error
        yield messages
    except error:
        yield error

def save_message(db:Session, request: RequestBaseModel):
    try:
        messages = crud.create(db, request)
        if not messages:
            error = True
        yield error
        yield messages
    except error:
        return error