import importlib
import os

# Dynamically import all models from subdirectories
def import_all_models():
    current_dir = os.path.dirname(__file__)
    for module_name in os.listdir(current_dir):
        module_path = os.path.join(current_dir, module_name)
        if os.path.isdir(module_path) and os.path.exists(os.path.join(module_path, 'models.py')):
            importlib.import_module(f".{module_name}.models", package=__package__)

# Call the function to ensure all models are imported
import_all_models()