# Vector Stores in LangChain — Complete Notes

## Why Vector Stores Exist

Traditional keyword search fails at semantic understanding.

Example:
A movie recommender cannot understand meaning using keywords alone.

Solution:
Convert text into embeddings (numerical vectors)
and compare meaning using vector similarity.

Problem after embeddings:

- millions of vectors to store
- high dimensional search
- need fast retrieval

Vector stores solve this.

---

## What is a Vector Store?

A Vector Store is a system designed to store and retrieve embeddings efficiently.

It enables semantic search instead of keyword search.

Core features:

- vector storage
- similarity search
- indexing
- metadata storage
- CRUD operations

Each stored item:

vector + original text + metadata

---

## How Vector Search Works

Text → Embedding → Vector

Query → Embedding → Compare vectors

Closest vectors = most similar meaning

Similarity methods:

- cosine similarity
- dot product
- euclidean distance

Goal:
Find semantic neighbors in vector space.

---

## Vector Store vs Vector Database

Vector Store:
- lightweight library
- focused on embeddings + search
- ideal for prototypes

Vector Database:
- full database system
- distributed architecture
- durability
- authentication
- transaction guarantees
- scaling

Simple rule:

Vector DB = Vector Store + database features

---

## Use Cases

- semantic search
- RAG systems
- recommender systems
- chatbot memory
- document search
- multimedia retrieval

Vector stores are the backbone of RAG.

---

## Vector Stores in LangChain

LangChain provides a common interface
for multiple vector backends.

You can switch vector stores
without changing application logic.

Supported stores include:

- Chroma
- FAISS
- Pinecone
- Weaviate
- Milvus
- Qdrant

This abstraction enables flexibility.

---

## Chroma Vector Store

ChromaDB is:

- lightweight
- open-source
- local-first
- beginner-friendly
- production capable for small scale

Ideal for:

- learning
- prototypes
- local RAG apps

---

## Chroma Hands-on Example

```python
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

docs = [
    Document(page_content="AI is changing the world"),
    Document(page_content="Cricket is popular in India"),
]

embeddings = OpenAIEmbeddings()

db = Chroma(
    collection_name="demo",
    embedding_function=embeddings,
    persist_directory="./chroma_db"
)

db.add_documents(docs)

results = db.similarity_search("technology and AI")

for r in results:
    print(r.page_content)
```

---

## Important Chroma Operations

Add documents:

db.add_documents(docs)

Retrieve all:

db.get()

Similarity search:

db.similarity_search(query)

Similarity search with score:

db.similarity_search_with_score(query)

Filter by metadata:

db.similarity_search(query, filter={"source": "pdf"})

Update:

db.update_documents(ids, docs)

Delete:

db.delete(ids)

---

## Interview Key Points

- Vector stores enable semantic retrieval
- Embeddings represent meaning numerically
- Similar vectors = similar ideas
- Vector DB adds scaling + durability
- Chroma is ideal for local development
- LangChain abstracts vector backends

---

## 20-Second Interview Summary

Vector stores store embeddings and enable fast similarity search.
They are essential for RAG systems because they allow semantic retrieval
instead of keyword matching.

---

## Quick Cheat Sheet

Vector store = embedding search engine

Embeddings → stored as vectors  
Query → converted to vector  
Nearest vector → answer context  

Chroma = local vector DB  
FAISS = fast in-memory search  
Pinecone = cloud vector DB  

Vector store = brain of RAG

