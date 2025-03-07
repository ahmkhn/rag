# models/document.py
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class Document(BaseModel):
    title: str = Field(..., description="The title of the document")
    content: str = Field(..., description="The main body of the document")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict, 
                                                 description="Optional metadata for the document")
