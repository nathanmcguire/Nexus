from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

# Define a basic route
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Define another route that accepts a path parameter
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}