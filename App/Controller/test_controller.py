from sqlalchemy.orm import Session

from ..Modules.mqtt_publisher import CLIENT, publish
from .schemas import MessageBaseModel
from ..Models.models import Message
from ..Models import crud

# Application controller layer


def get_all_messages(db: Session) -> list[Message] | Message | bool:
    """
    This function use database orm read function to try giving data from database

    Args:
        db (Session): database session with orm session type

    Returns:
        list[Message] | Message | bool: a list of messages or a message or boolean
    """
    try:  # try connecting database and give data
        messages = crud.read(db)
        if not messages:  # handling error
            not_error = False
        return messages
    except not_error:
        return not_error


def save_message(db: Session, request: MessageBaseModel) -> bool:
    """
    This function use database orm create function to try saving data to database

    Args:
        db (Session): database session with orm session type
        request (MessageBaseModel): request base model

    Returns:
        bool: result of saving data with True or False value
    """
    try:  # try connecting database and save data
        result = crud.create(db, request)
        if not result:  # handling error
            not_error = False
        return result
    except not_error:
        return not_error


async def connect_mqtt_broker() -> None | bool:
    """
    This function runs a mqtt connection and set a connection living loop

    Returns:
        None | bool: None or False
    """
    try:
        result = CLIENT.loop_start()
        if not result:
            not_error = False
    except not_error:
        return not_error


async def send_message(request: MessageBaseModel) -> str | bool:
    """
    This function send a message to publish and send to broker

    Args:
        request (MessageBaseModel): request base model

    Returns:
        str | bool: returns a published message string or a boolean variable
    """
    try:

        result = publish(CLIENT, request.micro_op, request.imei)
        if not result:
            not_error = False
        return result
    except not_error:
        return not_error
