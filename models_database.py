"""
Database Models

This file contains all SQLAlchemy models.

Currently:
- User
"""
# configurtion of the folder structure and path is pending rn its just in root dir

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Integer, String

from database_config import Base


class User(Base):
    """
    User table
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    name = Column(String(100), nullable=False)

    username = Column(String(50), unique=True, nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    password_hash = Column(String(255), nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )