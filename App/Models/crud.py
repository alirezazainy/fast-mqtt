from sqlalchemy.orm import Session
from .models import Message
from ..Controller.schemas import MessageBaseModel

# CRUD ORM functions


def create(db: Session, request: MessageBaseModel) -> bool:
    """
    This function saves data to database

    Args:
        db (Session): database session with orm session type
        request (MessageBaseModel): request base model

    Returns:
        bool: return true if completely finished
    """
    message = Message(imei=request.imei, micro_op=request.micro_op)  # -> add instance
    # add instance to database
    db.add(message)
    db.commit()
    db.refresh(message)
    return True


def read(
    db: Session, request: MessageBaseModel | None = None
) -> list[Message] | Message:
    """
    This function read items from database

    if you give a request model, the function searches in the database for a list of messages you give the imei or micro operation
        or give a message with ID

    Args:
        db (Session): database session with orm session type
        request (MessageBaseModel | None, optional): request base model. Defaults to None.

    Returns:
        list[Message] | Message: return a list of messages or a message
    """
    if request is not None:
        if request.id is not None:
            # search in ids
            return db.query(Message).filter(Message.ID == request.id).first()
        else:
            # search in imeis and micro ops
            return (
                db.query(Message)
                .filter(
                    Message.imei == request.imei
                    or Message.micro_op == request.micro_op
                )
                .order_by(Message.time_stamp)
                .all()
            )
    else:
        # get all of the database messages
        return db.query(Message).all()
