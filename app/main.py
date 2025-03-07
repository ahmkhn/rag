from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from endpoints.documents import router as documents_router

app = FastAPI()
app.include_router(documents_router)
