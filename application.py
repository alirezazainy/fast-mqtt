from fastapi import FastAPI, status
from Models.schemas import RequestModel, ResponseModel
from Modules.mqtt_publisher import send, run
#TODO: generate new request for get all entities from database 
#TODO: generate controllers
#TODO: complete fastapi write examples for swagger ui and redoc for better documenting and add doc strings
#TODO: generate mkdocs documenting

app = FastAPI()


@app.on_event("startup")
async def on_startup():
   await run()

@app.post("/", response_model=ResponseModel)
async def post(request: RequestModel) -> ResponseModel:
    response = ResponseModel
    response.message = await send(request.message)
    response.status_code = status.HTTP_200_OK
    response.topic = "python/mine"
    response.method = "POST"
    return response
    
@app.get("/{input_message}", response_model=ResponseModel)
async def path_parameter(input_message: str) -> ResponseModel:
    response = ResponseModel
    response.message = await send(input_message)
    response.status_code = status.HTTP_200_OK
    response.topic = "python/mine"
    response.method = "GET/PP"
    return response
    
@app.get("/", response_model=ResponseModel)
async def query_parameter(input_message: str) -> ResponseModel:
    response = ResponseModel
    response.message = await send(input_message)
    response.status_code = status.HTTP_200_OK
    response.topic = "python/mine"
    response.method = "GET/QP"
    return response