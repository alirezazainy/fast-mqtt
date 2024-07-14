from fastapi import FastAPI, status, Depends
from databa
from sqlalchemy.orm import Session
from .Controller.schemas import RequestBaseModel, ResponseModel
from Modules.mqtt_publisher import send_message, connect_mqtt_broker
from .Controller.test_controller import save_info
#TODO: generate new request for get all entities from database 
#TODO: generate controllers
#TODO: complete fastapi write examples for swagger ui and redoc for better documenting and add doc strings
#TODO: generate mkdocs documenting

app = FastAPI()


@app.on_event("startup")
async def on_startup() -> None:
    """
    This function starts mqtt connection at startup time of application
    """
    await connect_mqtt_broker()

# @app.post("/", response_model=ResponseModel)
# async def post(request: RequestModel) -> ResponseModel:
#     response = ResponseModel
#     response.message = await send_message(request.message)
#     response.status_code = status.HTTP_200_OK
#     response.topic = "python/mine"
#     response.method = "POST"
#     return response
    
# @app.get("/{input_message}", response_model=ResponseModel)
# async def path_parameter(input_message: str) -> ResponseModel:
#     response = ResponseModel
#     response.message = await send_message(input_message)
#     response.status_code = status.HTTP_200_OK
#     response.topic = "python/mine"
#     response.method = "GET/PP"
#     return response
    
# @app.get("/", response_model=ResponseModel)
# async def query_parameter(input_message: str) -> ResponseModel:
#     response = ResponseModel
#     response.message = await send_message(input_message)
#     response.status_code = status.HTTP_200_OK
#     response.topic = "python/mine"
#     response.method = "GET/QP"
#     return response

@app.get("/mqtt/{imei}/{micro_op}")
async def message(imei: str, micro_op: str, db: Session = Depends(get)):
    request = RequestBaseModel
    request.imei = imei
    request.micro_op = micro_op
    if save_info(db, request):
        
    await send_message
    
    