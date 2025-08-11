from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    database_url: str = "postgresql://postgres:postgres@localhost:5432/fastapi_db"
    keycloak_server_url: str = "http://localhost:8080"
    keycloak_realm: str = "myrealm"
    keycloak_client_id: str = "myclient"
    keycloak_client_secret: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()