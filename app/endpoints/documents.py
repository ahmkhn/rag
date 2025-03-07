# app/endpoints/documents.py
from fastapi import APIRouter, HTTPException
from models.document import Document
from services.document_service import process_document

router = APIRouter()

@router.post("/documents", response_model=dict)

async def create_document(document: Document):
    """
    Endpoint to receive a document, process it into text chunks, generate embeddings, 
    and add them to the FAISS index.
    """
    try:
        result = process_document(document)
        return {"message": "Document processed successfully", **result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
