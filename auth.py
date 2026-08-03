"""
auth.py

Purpose:
---------
Contains all authentication-related API endpoints.

Current Endpoints:
1. Signup
2. Login
"""

# FastAPI
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
# SQLAlchemy
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
# Database
from database_config import get_db

# Schemas
from schemas import UserSignup, UserLogin

# CRUD
from crud import (
    get_user_by_username,
    get_user_by_email,
    create_user,
)

import os
from dotenv import load_dotenv

# Password Manager
from password_manager import hash_password, verify_password

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")  # Use a strong secret in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

def create_access_token(data: dict, expires_delta: timedelta = None):
        """Generate a JWT access token."""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt


@router.post("/signup",status_code=status.HTTP_201_CREATED,)
def signup(user: UserSignup,db: Session = Depends(get_db),):
    """
    Register a new user.

    Flow:
    1. Validate request (Handled by Pydantic)
    2. Check if username already exists
    3. Check if email already exists
    4. Hash password
    5. Create user
    6. Return success response
    """

    # Check if username already exists
    existing_user = get_user_by_username(
        db=db,
        username=user.username,
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already exists.",
        )

    # Check if email already exists
    existing_email = get_user_by_email(
        db=db,
        email=user.email,
    )

    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered.",
        )

    # Hash the password
    hashed_password = hash_password(user.password)

    # Create the user
    new_user = create_user(
        db=db,
        name=user.name,
        username=user.username,
        email=user.email,
        password_hash=hashed_password,
    )

    # Return success response
    return {
        "message": "User created successfully.",
        "user_id": new_user.id,
        "username": new_user.username,
        "email": new_user.email,
    }


@router.post("/login")
def login(user: UserLogin,db: Session = Depends(get_db),):
    """ Authenticate a user and return a JWT token.
    Flow:
    1. Validate request (Handled by Pydantic)
    2. Check if username exists
    3. Verify password
    4. Generate JWT token
    5. Return token
    """
    # Check if user exists
    db_user = get_user_by_username(db=db, username=user.username)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Verify password
    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": db_user.username})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": db_user.id,
        "username": db_user.username,
        }
        



    