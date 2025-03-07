# services/query_service.py
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

from services.document_service import faiss_index, index_metadata, model  # Reuse globals from document processing

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

# 1. Generate query embedding
def get_query_embedding(query: str):
    # Reuse our SentenceTransformer to get the embedding for the query
    return model.encode([query])[0]

# 2. Search the FAISS index
def search_index(query_embedding, k=3):
    query_vec = np.array([query_embedding]).astype("float32")
    distances, indices = faiss_index.search(query_vec, k)
    results = []
    for idx in indices[0]:
        # Retrieve chunk if metadata exists for the index
        if idx in index_metadata:
            results.append(index_metadata[idx])
    return results

# 3. Set up LLM chain using GPT-4o-mini
prompt_template = """You are a knowledgeable assistant.
Use the following context to answer the question. If you're unsure, simply state that you don't know.

Context:
{context}

Question: {question}

Answer:"""
prompt = PromptTemplate.from_template(prompt_template)
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
llm_chain = LLMChain(llm=llm, prompt=prompt)

# 4. Process the query end-to-end
def process_query(query: str, k=3):
    # Generate the embedding for the incoming query
    query_embedding = get_query_embedding(query)
    # Search FAISS index for top-k similar document chunks
    relevant_chunks = search_index(query_embedding, k)
    # Concatenate the retrieved chunks to form the context; using key "chunk_text" from our metadata
    context = "\n".join([chunk["chunk_text"] for chunk in relevant_chunks])
    # Generate answer using the LLM chain
    answer = llm_chain.run(question=query, context=context)
    return {"query": query, "answer": answer, "context": relevant_chunks}
