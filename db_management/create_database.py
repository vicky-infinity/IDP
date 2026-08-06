"""
Create Database

Run this file only once.

It will:

1. Connect to SQLite
2. Read all database models
3. Create every table
"""
# configurtion of the folder structure and path is pending rn its just in root dir

from db_management.database_config import Base, engine
from db_management.models_database import User

# Create all tables
Base.metadata.create_all(bind=engine)

print("Database and tables created successfully!")