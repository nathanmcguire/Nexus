# filepath: c:\Users\nmcguire\Documents\GitHub\nexus\nexus-fastapi\main.py
import sys
import os

import assets.routes

# Add the nexus-fastapi directory to the Python module search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
import assets


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

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

# Include routers for modular route handling
app.include_router(assets.routes.router)
#app.include_router(users.router)
