# Embedding Models — Notes

## What is an Embedding?

An embedding is a numerical vector representation of text.

It converts words/sentences into numbers so machines can understand semantic meaning.

Example:

Text:
"Virat Kohli is a batsman"

Embedding (vector):
[0.12, -0.44, 0.18, 0.02, ...]

Each number represents a dimension of meaning.

Similar meaning → vectors close together  
Different meaning → vectors far apart

---

## Why Embeddings Matter

Embeddings are used for:

- Semantic search
- RAG (Retrieval-Augmented Generation)
- Chatbots with documents
- Recommendation systems
- Clustering documents
- Similarity matching
- AI assistants

They allow computers to compare meaning using math.

---

## Embedding Workflow

Text → Embedding Model → Vector → Similarity Search

Steps:

1. Convert documents into vectors
2. Convert query into vector
3. Compare vectors using cosine similarity
4. Retrieve most relevant document

---

## Cosine Similarity

Cosine similarity measures angle between vectors.

Formula intuition:

- 1 → identical meaning
- 0 → unrelated
- -1 → opposite meaning

Higher score = more similar.

---

## Types of Embedding Models

### 1. API-based embeddings

Cloud hosted models.

Examples:

- Google Gemini embeddings
- OpenAI embeddings

Pros:
- High quality
- No local compute needed

Cons:
- Paid after free quota
- Requires internet

---

### 2. Local embeddings

Run on your machine.

Example:

sentence-transformers/all-MiniLM-L6-v2

Pros:
- Free
- Offline
- Private

Cons:
- Uses CPU/GPU
- Slightly slower

---

## Gemini Embedding Example

```python
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

vector = embedding.embed_query("Tell me about cricket")
