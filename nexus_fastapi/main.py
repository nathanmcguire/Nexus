from fastapi import FastAPI
from .database import engine, Base
from .domains.models import *
from .domains.routes import register_routes
from .exceptions import *
from .logging import configure_logging, LogLevels

configure_logging(LogLevels.info)

app = FastAPI(
    title="Nexus",
    description="",
    summary="",
    #contact={
        #"name": "",
        #"url": "",
        #"email": "",
    #},
    license_info={
        "name": "",
        "identifier": "MIT",
    }
)

register_routes(app)
