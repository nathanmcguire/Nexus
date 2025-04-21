from .users.controllers import router as users_router
from .auth.controllers import router as auth_router

def register_routes(app):
    """
    Register all the routes for the FastAPI application.
    """
    app.include_router(users_router)
    app.include_router(auth_router)