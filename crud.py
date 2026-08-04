"""
crud.py

Purpose:
---------
Contains all database operations for the User table.
"""

from sqlalchemy.orm import Session
from models_database import User


def get_user_by_username(db: Session, username: str):
    """
    Returns the user if the username exists.
    Otherwise returns None.
    """
    return (db.query(User).filter(User.username == username).first())


def get_user_by_email(db: Session, email: str):
    """
    Returns the user if the email exists.
    Otherwise returns None.
    """
    return (db.query(User).filter(User.email == email).first())


def create_user(db: Session,name: str,username: str,email: str,password_hash: str,):
    """
    Creates a new user in the database.
    """

    # Create a User object
    new_user = User(
        name=name,
        username=username,
        email=email,
        password_hash=password_hash,
    )

    # Add the object to the current session
    db.add(new_user)

    # Save changes to the database
    db.commit()

    # Refresh the object to get generated values
    # like id and created_at
    db.refresh(new_user)

    # Return the created user
    return new_user