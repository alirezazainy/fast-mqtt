from fastapi import FastAPI
from .Database.database import engine
from .Controller.test_controller import connect_mqtt_broker
from .Models.models import Base
from fastapi.middleware.cors import CORSMiddleware
from .Routers import messaging, reporting

# Main Application

# TODO: complete fastapi write examples for swagger ui and redoc for better documenting and add doc strings
# TODO: generate mkdocs documenting

# Generate FastAPI app
app = FastAPI(
    title="Fast-MQTT",
    summary="Fast MQTT web API messenger based on FastAPI",
    description="Faster and newer than other",
    version="0.5.6",
)
# Include routers
app.include_router(messaging.router)
app.include_router(reporting.router)
# Generate database engine
Base.metadata.create_all(engine)
# Handling CORS errors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:8080", "https://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# On startup mqtt broker connection
@app.on_event("startup")
async def on_startup() -> None:
    """
    This function starts mqtt connection at startup time of application
    """
    await connect_mqtt_broker()


@app.get("/")
async def start_page():
    return "Coded with Galb:)"


# Coded With Galb:)
# Bachelor of Computer Engineering Alireza Zainy
