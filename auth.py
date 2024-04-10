from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer   #auth using bearer token
from fastapi.responses import JSONResponse 
from typing import Annotated

# all routes that start with /auth/...
router = APIRouter(prefix="/auth")

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@router.get("/admin/dash")
def handle_dash(
    token: Annotated[str, Depends(oauth_scheme)]
):
    return JSONResponse(token)

# we need to install python-jose for JWT and passlib for hashing
"""
pip install "passlib[bcrypt]"
pip install "python-jose[cryptography]"
"""

from jose import jwt, JWTError
from passlib.context import CryptContext

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

password_context = CryptContext(schemes=["bcrypt"])

def verify(plain, hashed):
    return password_context.verify(plain, hashed)

def get_password_hash(password):
    return password_context.hash(password)
