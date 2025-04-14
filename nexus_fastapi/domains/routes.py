import importlib
import os
from fastapi import FastAPI

def register_routes(app: FastAPI) -> None:
    # Dynamically find and include routers from submodules
    domains_path = os.path.dirname(__file__)
    for module_name in os.listdir(domains_path):
        module_path = os.path.join(domains_path, module_name)
        if os.path.isdir(module_path):
            # Check for routes.py
            if os.path.exists(os.path.join(module_path, 'routes.py')):
                module = importlib.import_module(f".{module_name}.routes", package=__package__)
                if hasattr(module, 'router'):
                    app.include_router(module.router)
            # Check for controllers.py
            if os.path.exists(os.path.join(module_path, 'controllers.py')):
                module = importlib.import_module(f".{module_name}.controllers", package=__package__)
                if hasattr(module, 'router'):
                    app.include_router(module.router)