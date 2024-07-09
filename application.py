from fastapi import FastAPI
from Model.schemas import RequestModel
from Modules.mqtt_publisher import run, send

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await run()

@app.post("/")
async def mmd(request: RequestModel):
    await send(request.message)
    return {
        "msg": request.message
    }