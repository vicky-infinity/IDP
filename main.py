"""
main.py

Purpose:
---------
Entry point of the FastAPI application.

This file:
1. Creates the FastAPI application
2. Registers all routers
"""

from fastapi import FastAPI

from auth import router
from file_processes.process_files import fprouter

app = FastAPI(
    title="Authentication API",
    version="1.0.0",
    description="IDP Backend API"
)
app.include_router(router)
app.include_router(fprouter)