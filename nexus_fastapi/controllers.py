from .users.controllers import router as users_router

def register_routes(app):
    """
    Register all the routes for the FastAPI application.
    """
    app.include_router(users_router)