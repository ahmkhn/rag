# services/document_service.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from utils.text_processing import split_text_into_chunks

# Define the embedding dimension (depends on the model; for "all-MiniLM-L6-v2", it's 384)
EMBEDDING_DIM = 384

# Create a global FAISS index instance (using L2 distance)
faiss_index = faiss.IndexFlatL2(EMBEDDING_DIM)

# Optionally, maintain a simple dictionary mapping each vector id to its metadata
index_metadata = {}

# Load the pre-trained SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def process_document(document, chunk_size: int = 3, overlap: int = 1):
    """
    Processes a document by splitting it into chunks, generating embeddings for each chunk, 
    and adding them to the FAISS index along with metadata.
    
    Args:
        document: An object with attributes 'title', 'content', and 'metadata'.
        chunk_size (int): Number of sentences per chunk.
        overlap (int): Number of overlapping sentences.
    
    Returns:
        dict: Information about processing, including number of chunks and their corresponding indices.
    """
    # 1. Split text into chunks
    chunks = split_text_into_chunks(document.content, method='sentence', chunk_size=chunk_size, overlap=overlap)
    
    # 2. Generate embeddings using SentenceTransformers
    chunk_embeddings = model.encode(chunks)  # Output shape: (n_chunks, EMBEDDING_DIM)
    embeddings_np = np.array(chunk_embeddings, dtype='float32')
    
    # 3. Add embeddings into the FAISS index
    start_id = int(faiss_index.ntotal)  # starting index id for this document
    faiss_index.add(embeddings_np)
    
    # 4. Store metadata for each chunk
    for i, chunk in enumerate(chunks):
        vector_id = start_id + i
        index_metadata[vector_id] = {
            "document_title": document.title,
            "chunk_text": chunk,
            "document_metadata": document.metadata
        }
    
    return {"n_chunks": len(chunks), "added_vector_ids": list(range(start_id, start_id + len(chunks)))}
