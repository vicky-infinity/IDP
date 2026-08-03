"""
Database Configuration

This file is responsible for:

1. Loading the database URL
2. Creating the SQLAlchemy Engine
3. Creating SessionLocal
4. Creating Base

Every database model will inherit from Base.
Every database operation will use SessionLocal.
"""
# configurtion of the folder structure and path is pending rn its just in root dir

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Load environment variables
load_dotenv()

# Read database URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Create database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for all models
Base = declarative_base()