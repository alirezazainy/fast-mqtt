from fastapi import FastAPI, status, Depends, HTTPException
from Database.database import get_db, engine
from sqlalchemy.orm import Session
from Controller.schemas import RequestBaseModel, ResponseModel
from Modules.mqtt_publisher import connect_mqtt_broker, send_message
from Controller.test_controller import save_message, get_all_messages
from Models.models import Base
from fastapi.middleware.cors import CORSMiddleware
#TODO: generate new request for get all entities from database 
#TODO: generate controllers
#TODO: complete fastapi write examples for swagger ui and redoc for better documenting and add doc strings
#TODO: generate mkdocs documenting

app = FastAPI()

Base.metadata.create_all(engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:8080",
        "https://localhost"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
async def on_startup() -> None:
    """
    This function starts mqtt connection at startup time of application
    """
    await connect_mqtt_broker()

# @app.post("/", response_model=ResponseModel)
# async def post(request: RequestModel) -> ResponseModel:
#     response = ResponseModel
#     response.message = await save_message(request.message)
#     response.status_code = status.HTTP_200_OK
#     response.topic = "python/mine"
#     response.method = "POST"
#     return response
    
# @app.get("/{input_message}", response_model=ResponseModel)
# async def path_parameter(input_message: str) -> ResponseModel:
#     response = ResponseModel
#     response.message = await save_message(input_message)
#     response.status_code = status.HTTP_200_OK
#     response.topic = "python/mine"
#     response.method = "GET/PP"
#     return response
    
# @app.get("/", response_model=ResponseModel)
# async def query_parameter(input_message: str) -> ResponseModel:
#     response = ResponseModel
#     response.message = await save_message(input_message)
#     response.status_code = status.HTTP_200_OK
#     response.topic = "python/mine"
#     response.method = "GET/QP"
#     return response

@app.get("/mqtt/{imei}/{micro_op}")
async def message(imei: str, micro_op: str, db: Session = Depends(get_db)):
    request = RequestBaseModel
    request.imei = imei
    request.micro_op = micro_op
    data = save_message(db, request)
    if not data:
        raise HTTPException(status.WS_1005_NO_STATUS_RCVD, "Something went wrong")
    else:
        result = await send_message(f"{request.imei}/{request.micro_op}")
        raise HTTPException(status.HTTP_201_CREATED, result)

@app.get("/all",response_model=list[ResponseModel])
async def get_all(db: Session = Depends(get_db)):
    messages = get_all_messages(db)
    return messages
    
    