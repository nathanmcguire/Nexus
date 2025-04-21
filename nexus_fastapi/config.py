"""
Configuration module for the nexus_fastapi application.

This module defines the `Settings` class, which is used to manage application
configuration using environment variables and default values. It also includes
helper functions and constants for database and server configuration.

Classes:
    Settings: A Pydantic BaseSettings class for managing application settings.

Functions:
    parse_cors(v: Any) -> list[str] | str: Parses CORS origins from a string or list.

Constants:
    settings: An instance of the `Settings` class.

Notes:
    Ensure that environment variables are properly set in the `.env` file for
    the application to function correctly.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from typing import Annotated, Any, Literal
from pydantic import AnyUrl, BeforeValidator, computed_field

# Load environment variables from .env file
load_dotenv()


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):
    """
    Application settings managed via environment variables.

    Attributes:
        SECRET_KEY (str): Secret key for cryptographic operations.
        ALGORITHM (str): Algorithm used for token encoding.
        ACCESS_TOKEN_EXPIRE_MINUTES (int): Token expiration time in minutes.
        DATABASE_URL (str): URL for the database connection.
        DOMAIN (str): Domain name of the application.
        ENVIRONMENT (Literal): Deployment environment (local, staging, production).
        BACKEND_CORS_ORIGINS (list[AnyUrl] | str): Allowed CORS origins.
        POSTGRESQL_USER (str): PostgreSQL username.
        POSTGRESQL_PASSWORD (str): PostgreSQL password.
        POSTGRESQL_SERVER (str): PostgreSQL server address.
        POSTGRESQL_PORT (int): PostgreSQL server port.
        POSTGRESQL_DB (str): PostgreSQL database name.
        MYSQL_USER (str): MySQL username.
        MYSQL_PASSWORD (str): MySQL password.
        MYSQL_SERVER (str): MySQL server address.
        MYSQL_PORT (int): MySQL server port.
        MYSQL_DB (str): MySQL database name.

    Methods:
        server_host: Returns the server host URL based on the environment.
        SQLALCHEMY_DATABASE_URI: Constructs the SQLAlchemy database URI based on the environment.
    """
    SECRET_KEY: str = "your-secret-key"  # Replace with a secure key
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "sqlite:///./sqlite.db"

    model_config = SettingsConfigDict(env_file='.env', env_ignore_empty=True, extra="ignore")
    DOMAIN: str = 'localhost'
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"

    @computed_field
    @property
    def server_host(self) -> str:
        """
        Compute the server host URL based on the environment.

        Returns:
            str: The server host URL.
        """
        # Use HTTPS for anything other than local development
        if self.ENVIRONMENT == "local":
            return f"http://{self.DOMAIN}"
        return f"https://{self.DOMAIN}"

    BACKEND_CORS_ORIGINS: Annotated[
        list[AnyUrl] | str, BeforeValidator(parse_cors)
    ] = []

    POSTGRESQL_USER: str = "postgres"
    POSTGRESQL_PASSWORD: str = "password"
    POSTGRESQL_SERVER: str = "localhost"
    POSTGRESQL_PORT: int = 5432
    POSTGRESQL_DB: str = "app_db"

    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "password"
    MYSQL_SERVER: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_DB: str = "app_db"

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        """
        Construct the SQLAlchemy database URI based on the environment.

        Returns:
            str: The SQLAlchemy database URI.

        Raises:
            ValueError: If the environment configuration is invalid.
        """
        if self.ENVIRONMENT == "local":
            return "sqlite:///./sqlite.db"
        elif self.ENVIRONMENT == "staging":
            return f"postgresql://{self.POSTGRESQL_USER}:{self.POSTGRESQL_PASSWORD}@{self.POSTGRESQL_SERVER}:{self.POSTGRESQL_PORT}/{self.POSTGRESQL_DB}"
        elif self.ENVIRONMENT == "production":
            return f"mysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_SERVER}:{self.MYSQL_PORT}/{self.MYSQL_DB}"
        raise ValueError("Invalid environment configuration")


settings = Settings()
