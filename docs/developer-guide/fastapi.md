# FastAPI

## Overview
This document provides an overview of the FastAPI backend included in the Nexus project. The backend is responsible for handling API requests, managing the database, and serving as the core of the application.

## Project Structure

| Folder/File Path         | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| `fastapi/`               | Contains the main FastAPI application files.                              |
| `fastapi/main.py`        | Entry point for the FastAPI application.                                   |
| `fastapi/config.py`      | Configuration settings for the application.                                |
| `fastapi/controllers.py` | API route handlers for various endpoints.                                 |
| `fastapi/database.py`    | Database connection and session management.                               |
| `fastapi/models.py`      | SQLAlchemy models for database tables.                                     |
| `fastapi/schemas.py`     | Pydantic schemas for request and response validation.                      |
| `fastapi/assets/`        | Contains additional modules for assets-related functionality.              |

## Key Features
- **FastAPI Framework**: High-performance web framework for building APIs.
- **SQLAlchemy Integration**: ORM for database interactions.
- **Pydantic Validation**: Data validation and serialization using Pydantic.
- **Modular Design**: Organized into controllers, models, schemas, and services.

## Development Setup
1. **Requirements**:
   - Python 3.9 or higher.
   - Virtual environment (recommended).
2. **Steps**:
   - Install dependencies: `pip install -r requirements.txt`.
   - Run the application: `uvicorn fastapi.main:app --reload`.

## API Endpoints
- **Users**: Manage user accounts and authentication.
- **Devices**: Handle device-related operations.
- **Documents**: Manage document storage and retrieval.
- **Network**: Network-related functionalities.
- **Software**: Software-related operations.

## API Documentation
- **Swagger UI**: Available at `/docs` for interactive API exploration.
- **ReDoc**: Available at `/redoc` for detailed API documentation.

## Testing
- Use `pytest` for running test cases.
- Test files are located in the `tests/fastapi/` directory.

## Deployment
- Use a production-ready ASGI server like `uvicorn` or `gunicorn`.
- Configure environment variables for production settings.

## Additional Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)