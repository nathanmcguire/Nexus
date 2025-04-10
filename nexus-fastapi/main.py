<<<<<<< Updated upstream
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
=======
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.session import engine
from db.base import Base
from api.v1.endpoints import auth, protected

# Initialize the database tables
Base.metadata.create_all(bind=engine)

# Create the FastAPI app
app = FastAPI(
    title="Nexus FastAPI",
    description="A FastAPI application with authentication and authorization",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(protected.router, prefix="/protected", tags=["Protected Routes"])

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to Nexus FastAPI!"}
>>>>>>> Stashed changes
