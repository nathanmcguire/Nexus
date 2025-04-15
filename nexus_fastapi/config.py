from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
from typing import Annotated, Any, Literal
from pydantic import AnyUrl, BeforeValidator, computed_field, PostgresDsn
from pydantic_core import MultiHostUrl

# Load environment variables from .env file
load_dotenv()

def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)

class Settings(BaseSettings):
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
        if self.ENVIRONMENT == "local":
            return "sqlite:///./sqlite.db"
        elif self.ENVIRONMENT == "staging":
            return f"postgresql://{self.POSTGRESQL_USER}:{self.POSTGRESQL_PASSWORD}@{self.POSTGRESQL_SERVER}:{self.POSTGRESQL_PORT}/{self.POSTGRESQL_DB}"
        elif self.ENVIRONMENT == "production":
            return f"mysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_SERVER}:{self.MYSQL_PORT}/{self.MYSQL_DB}"
        raise ValueError("Invalid environment configuration")

settings = Settings()