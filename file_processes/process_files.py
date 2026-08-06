from fastapi import FastAPI, HTTPException, APIRouter



fprouter = APIRouter(
    prefix="/File",
    tags=["File Data Extraction"],
)


