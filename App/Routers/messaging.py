from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from ..Database.database import get_db
from ..Controller.schemas import MessageBaseModel

from ..Controller.test_controller import save_message, send_message

# Messaging router


# Generate Router
router = APIRouter(prefix="/messaging", tags=["Messaging"])


@router.post("/send")
async def send_and_save_massage(
    request: MessageBaseModel, db: Session = Depends(get_db)
):
    """
    Save and send a mqtt message
    Args:
        imei (str): sender machine imei
        micro_op (str): micro operation for doing jobs
        db (Session, optional): database session. Defaults to Depends(get_db).

    Raises:
        HTTPException: 406 not acceptable request
        HTTPException: 201 create and send message
    """
    result = await send_message(request)  # -> sending message
    if result is not str:
        # send request to database for saving
        data = save_message(db, request)
        while not data:
            data = save_message(db, request)
        if not data:
            raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE, "Something went wrong")
        raise HTTPException(status.HTTP_201_CREATED, result)
    else:
        raise HTTPException(status.HTTP_406_NOT_ACCEPTABLE, "Something went wrong")
