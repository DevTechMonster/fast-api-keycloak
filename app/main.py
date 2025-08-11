from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from database import get_db, engine
from models import Base
from auth import verify_token, get_current_user
from config import settings
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI with Keycloak",
    description="A FastAPI application with PostgreSQL and Keycloak authentication",
    version="1.0.0"
)

security = HTTPBearer()

@app.get("/")
async def root():
    return {"message": "Hello World - FastAPI with Keycloak"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/protected")
async def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": f"Hello {current_user.get('preferred_username', 'User')}, this is a protected route"}

@app.get("/users/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )