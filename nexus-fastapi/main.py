# filepath: c:\Users\nmcguire\Documents\GitHub\nexus\nexus-fastapi\main.py
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import yaml
from .routes import assets, users

app = FastAPI()

# Include routers
app.include_router(assets.router)
app.include_router(users.router)

@app.get("/openapi.yaml", include_in_schema=False)
def get_openapi_yaml():
    """
    Returns the OpenAPI schema in YAML format.
    """
    openapi_schema = get_openapi(
        title="Nexus API",
        version="1.0.0",
        description="API documentation for Nexus",
        routes=app.routes,
    )
    return yaml.dump(openapi_schema, allow_unicode=True)
