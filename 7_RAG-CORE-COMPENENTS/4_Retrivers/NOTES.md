# Retrievers in LangChain — Complete Notes

## What is a Retriever?

A Retriever is a component that fetches relevant documents
from a knowledge source based on a user query.

It acts like a search engine inside a RAG system.

Retriever does NOT generate answers.
Retriever only returns context.

LLM uses retrieved context to generate the final response.

Mental model:

User Query → Retriever → Relevant Documents → LLM → Answer

Retriever = librarian  
LLM = writer

---

## Why Retrievers Matter

LLMs do not have real-time or private knowledge.

Retrievers allow:

- external knowledge access
- domain-specific search
- up-to-date information
- scalable document retrieval

Good retrieval = good RAG performance.

---

## Retriever vs Vector Store

Vector Store:
- stores embeddings
- performs similarity search

Retriever:
- abstraction layer over search
- standard interface
- integrates with chains

Vector Store → Retriever → LLM

Retriever simplifies pipeline design.

---

## Vector Store Retriever

Most common retriever in RAG systems.

It searches embeddings using semantic similarity.

Example:

```python
retriever = vector_store.as_retriever()
results = retriever.invoke("How do machines learn?")
```

Returns Document objects.

---

## Retriever Types

Retrievers differ by search strategy.

Each solves a different problem.

---

### 1. MMR Retriever (Maximum Marginal Relevance)

Problem:
Similarity search returns redundant documents.

MMR balances:
- relevance
- diversity

It avoids repeating the same information.

Example:

```python
retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3}
)
```

Use when:
- documents are similar
- you want diverse perspectives

Interview line:

MMR improves retrieval diversity while maintaining relevance.

---

### 2. Multi Query Retriever

Problem:
User queries are ambiguous.

Multi-query retriever:
- generates multiple sub-queries
- expands the search space
- improves recall

Example:

```python
from langchain.retrievers.multi_query import MultiQueryRetriever
retriever = MultiQueryRetriever.from_llm(llm, vector_store.as_retriever())
```

Use when:
- questions are vague
- recall matters more than precision

Interview line:

Multi-query retrieval expands ambiguous queries to improve recall.

---

### 3. Contextual Compression Retriever

Problem:
Retrieved documents are too long.

Compression retriever:
- removes irrelevant parts
- keeps only useful content

Reduces token usage.

Example:

```python
from langchain.retrievers import ContextualCompressionRetriever
```

Use when:
- documents are large
- token efficiency matters

Interview line:

Contextual compression reduces noise in retrieved context.

---

### 4. Wikipedia Retriever

Fetches documents directly from Wikipedia API.

No ingestion needed.

Example:

```python
from langchain.retrievers import WikipediaRetriever
retriever = WikipediaRetriever()
```

Use when:
- public knowledge search
- quick prototypes

---

## Retriever Architecture Insight

Different retrievers optimize different goals:

duplicate results → MMR  
ambiguous query → Multi-query  
long documents → Compression  
public knowledge → Wikipedia  
semantic search → Vector retriever

Real RAG systems combine strategies.

---

## Retriever Output

Retrievers return:

List[Document]

Each document contains:

- page_content
- metadata

Metadata enables citation and filtering.

---

## Interview Key Points

- Retriever fetches context, not answers
- Vector retriever is the most common
- MMR adds diversity
- Multi-query improves recall
- Compression reduces tokens
- Retrieval quality defines RAG performance

---

## 20-Second Interview Summary

Retrievers fetch relevant documents from a knowledge base.
They optimize search quality using strategies like diversity,
query expansion, and compression to improve RAG systems.

---

## Quick Cheat Sheet

Retriever = semantic search engine

Vector retriever → similarity search  
MMR → diversity  
Multi-query → recall  
Compression → efficiency  
Wikipedia → external knowledge

Retriever quality = RAG quality

