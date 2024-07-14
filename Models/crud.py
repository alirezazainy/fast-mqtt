from sqlalchemy.orm import Session
from .models import Messages
from ..Controller.schemas import RequestBaseModel
# CRUD ORM functions

def create(db: Session, request: RequestBaseModel):
    message = Messages(
        imei=request.imei,
        micro_op=request.micro_op
    )
    db.add(message)
    db.commit()
    db.refresh(message)

def read(db: Session, request: RequestBaseModel | None = None):
    if request is not None:
        if request.id is not None:
            return db.query(Messages).filter(Messages.ID == request.id).first()
        else:
            return db.query(Messages).filter(Messages.imei == request.imei or Messages.micro_op == request.micro_op).order_by(Messages.time_stamp).all()
    else:
        return db.query(Messages).all()

