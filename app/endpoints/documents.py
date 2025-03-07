from fastapi import APIRouter, HTTPException
from models.document import Document

router = APIRouter()

@router.post("/documents", response_model=Document)

async def create_document(document: Document):
    "we need to create a document from provided metadata & content"
    
    return document
