from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from app.endpoints.documents import router as documents_router
from app.endpoints.query import router as query_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(documents_router)
app.include_router(query_router)