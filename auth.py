"""
auth.py

Purpose:
---------
Contains all authentication-related API endpoints.

Current Endpoints:
1. Signup
"""

# FastAPI
from fastapi import APIRouter, Depends, HTTPException, status

# SQLAlchemy
from sqlalchemy.orm import Session

# Database
from database_config import get_db

# Schemas
from schemas import UserSignup

# CRUD
from crud import (
    get_user_by_username,
    get_user_by_email,
    create_user,
)

# Password Manager
from password_manager import hash_password


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/signup",
    status_code=status.HTTP_201_CREATED,
)
def signup(
    user: UserSignup,
    db: Session = Depends(get_db),
):
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