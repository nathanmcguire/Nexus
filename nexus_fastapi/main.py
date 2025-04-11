# filepath: c:\Users\nmcguire\Documents\GitHub\nexus\nexus-fastapi\main.py
import os
import sys

# Ensure the nexus_fastapi directory is in the Python module search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Ensure the assets directory is in the Python module search path
sys.path.append(os.path.join(os.path.dirname(__file__), 'assets'))

import assets.routes

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
