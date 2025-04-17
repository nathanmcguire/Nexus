# Create a new directory for tests
# Directory: c:\Users\nmcguire\Documents\GitHub\nexus\tests
# Add a test file for user endpoints
# File: c:\Users\nmcguire\Documents\GitHub\nexus\tests\test_users.py

import pytest
from fastapi.testclient import TestClient
from nexus_fastapi.main import app

client = TestClient(app)

# Test for getting all users
def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test for creating a user
def test_create_user():
    user_data = {
        "username": "testuser",
        "password": "testpassword",
        "is_active": True
    }
    response = client.post("/users", json=user_data)
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

# Test for getting a user by ID
def test_get_user_by_id():
    user_id = 1  # Replace with a valid user ID
    response = client.get(f"/users/{user_id}")
    if response.status_code == 200:
        assert response.json()["id"] == user_id
    else:
        assert response.status_code == 404

# Test for updating a user
def test_update_user():
    user_id = 1  # Replace with a valid user ID
    update_data = {
        "username": "updateduser",
        "is_active": False
    }
    response = client.patch(f"/users/{user_id}", json=update_data)
    if response.status_code == 200:
        assert response.json()["username"] == "updateduser"
    else:
        assert response.status_code == 404

# Test for deleting a user
def test_delete_user():
    user_id = 1  # Replace with a valid user ID
    delete_data = {
        "is_deleted": True
    }
    response = client.delete(f"/users/{user_id}", json=delete_data)
    if response.status_code == 200:
        assert response.json()["is_deleted"] is True
    else:
        assert response.status_code == 404