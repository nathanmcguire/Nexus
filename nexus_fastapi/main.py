from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .models import *
from .controllers import register_routes
from .exceptions import *
from .logging import configure_logging, LogLevels


configure_logging(LogLevels.info)

app = FastAPI(
    debug=True,
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
    },
    openapi_tags=[
        {"name": "Users", "description": "User Management", "endpoints": [
            {"operationId": "getUsers", "summary": "Get Users"},
            {"operationId": "createUser", "summary": "Create User"},
            {"operationId": "getUserById", "summary": "Get User By Id"},
            {"operationId": "replaceUserById", "summary": "Replace User By Id"},
            {"operationId": "updateUserById", "summary": "Update User By Id"},
            {"operationId": "deleteUserById", "summary": "Delete User By Id"},
        ]}
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8001", "http://localhost:3000"],  # Added React app origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_routes(app)
