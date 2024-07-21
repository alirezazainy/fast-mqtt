from fastapi import Depends, APIRouter
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from ..Database.database import get_db
from ..Controller.schemas import MessageBaseModel

from ..Controller.test_controller import get_all_messages

# Reporting router

# TODO: handle exceptions

# Generate router
router = APIRouter(prefix="/reporting", tags=["Reporting"])


@router.get("/all", response_model=list[MessageBaseModel])
async def get_all(db: Session = Depends(get_db)):
    """
    Get all entities from database
    Args:
        db (Session, optional): database session. Defaults to Depends(get_db).

    Returns:
        list[ResponseModel]: a list of messages organized with fastapi response model schema
    """
    # get all messages
    messages = get_all_messages(db)
    return messages
