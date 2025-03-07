# Cloud RAG AI Query Service

A containerized FastAPI microservice that implements **Retrieval-Augmented Generation (RAG)** for AI-powered query responses on documents such as PDFs or text files. This project leverages **FAISS** for vector-based retrieval, **SentenceTransformers** for embedding, and **OpenAI GPT** for generating contextually relevant answers. Deployed on **Azure** via Docker.

Example Curl & Response

![image](https://github.com/user-attachments/assets/12a93c01-1ea5-41db-bf42-a459080f417f)

![image](https://github.com/user-attachments/assets/a170a629-8ca6-4eab-8c02-faabf082cd35)



## Features

- **Document Upload & Chunking**  
  Upload PDFs or text files; the service automatically splits them into smaller chunks for efficient retrieval.

- **Vector-Based Retrieval with FAISS**  
  Creates embeddings using SentenceTransformers and stores them in FAISS, enabling fast and accurate search.

- **Context-Aware AI Responses**  
  Queries are augmented with retrieved context from your uploaded documents. The OpenAI GPT model then generates contextually relevant answers.

- **RESTful API with FastAPI**  
  A clean and interactive API, featuring auto-generated docs at `/<your_app>/docs` for quick testing.

- **Containerized & Deployed on Azure**  
  Dockerized for portability. Uses Azure App Service for easy deployment and scaling.

---

## Tech Stack

- **Language & Frameworks:**  
  - Python 3.10  
  - FastAPI  
  - FAISS & SentenceTransformers  
  - OpenAI GPT models (via `openai` or `langchain`)

- **Containerization & Deployment:**  
  - Docker & Docker Buildx (for linux/amd64 images)  
  - Azure App Service & Azure Container Registry  

- **Additional Tools & Libraries:**  
  - LangChain (for advanced LLM orchestration)  
  - Requests, pydantic, uvicorn  

---

## Architecture Overview

1. **Document Ingestion:**  
   Users upload documents (PDF/text). The service processes and splits them into smaller chunks.  

2. **Embedding & Storage:**  
   SentenceTransformers generate embeddings, which are stored in FAISS for quick nearest-neighbor lookups.  

3. **Query Processing:**  
   A user query is embedded and matched against stored chunks in FAISS.  

4. **LLM Generation:**  
   The retrieved context is passed to an OpenAI GPT model, which produces a context-aware answer.  

5. **Response:**  
   The service returns the AI-generated answer, along with any relevant metadata.

---
