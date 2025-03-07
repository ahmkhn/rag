# app/endpoints/query.py
from fastapi import APIRouter, HTTPException
from models.query import QueryRequest
from services.query_service import process_query

router = APIRouter()

@router.post("/query")
def query_document(request: QueryRequest):
    try:
        result = process_query(request.query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
