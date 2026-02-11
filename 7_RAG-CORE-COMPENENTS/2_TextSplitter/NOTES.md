# LangChain Text Splitters — Complete Notes

## What is a Text Splitter?

A text splitter is a component in LangChain that breaks large documents into smaller chunks.

LLMs cannot process very large documents effectively. Splitting ensures:
- manageable chunk sizes
- better embeddings
- accurate retrieval in RAG systems

Text splitting happens after document loading and before embeddings.

Pipeline:

Document Loader → Text Splitter → Embeddings → Vector DB → Retriever → LLM

---

## Why Text Splitting is Important

- prevents context overflow
- improves retrieval precision
- reduces hallucination
- preserves semantic meaning
- enables efficient embedding

Bad chunking = bad RAG performance.

---

## Types of Text Splitting

### 1. Character-Based Splitting

Splits text using character count.

Example splitter:
RecursiveCharacterTextSplitter

It tries to split intelligently using:

paragraph → sentence → word → character

This prevents breaking sentences unnecessarily.

Best for:
- general documents
- PDFs
- plain text ingestion

---

### RecursiveCharacterTextSplitter Example

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
```

Parameters:

- chunk_size → max characters per chunk
- chunk_overlap → repeated text between chunks

Overlap preserves context continuity.

---

### 2. Structure-Based Splitting

Splits based on document structure instead of character length.

Examples:

- MarkdownHeaderTextSplitter
- HTMLHeaderTextSplitter
- Code splitters

These respect headings and hierarchy.

Best for:
- documentation
- websites
- markdown files
- structured reports

Goal:
preserve semantic hierarchy.

---

### 3. Semantic Splitting

Uses embeddings to split based on meaning.

Example:
SemanticChunker

It compares sentence similarity and creates chunks when meaning changes.

```python
from langchain_experimental.text_splitter import SemanticChunker
```

Advantages:
- meaning-preserving chunks
- better retrieval quality

Disadvantages:
- slower
- requires embedding API
- threshold tuning needed

Best for:
- research papers
- legal documents
- long knowledge bases

---

## Document-Based Splitting

Text splitters operate on Document objects.

Each chunk remains a Document with metadata preserved.

Example metadata:

- source file
- page number
- section

This enables citation and traceability in RAG systems.

Important:
metadata is never lost during splitting.

---

## Markdown Header Text Splitter

MarkdownHeaderTextSplitter splits documents based on markdown headings.

It preserves document hierarchy and groups content under headers.

Example markdown:

# Title
Text...

## Section
Text...

Each header becomes a logical chunk boundary.

Best for:
- documentation
- README files
- knowledge bases
- structured notes

Example:

```python
from langchain_text_splitters import MarkdownHeaderTextSplitter

headers = [
    ("#", "Header 1"),
    ("##", "Header 2"),
]

splitter = MarkdownHeaderTextSplitter(headers)

chunks = splitter.split_text(markdown_text)
```

Advantages:
- respects structure
- preserves hierarchy
- better semantic grouping

Interview line:

Markdown splitting preserves document hierarchy for structured retrieval.

---

## HTML Header Text Splitter

HTMLHeaderTextSplitter splits web content using HTML tags.

It uses headers like:

- h1
- h2
- h3
- sections

to define chunk boundaries.

Best for:
- scraped websites
- blogs
- documentation portals
- web-based knowledge systems

Example:

```python
from langchain_text_splitters import HTMLHeaderTextSplitter

headers = [("h1", "Header 1"), ("h2", "Header 2")]

splitter = HTMLHeaderTextSplitter(headers)

chunks = splitter.split_text(html_text)
```

Advantages:
- respects webpage structure
- preserves sections
- improves retrieval relevance

Interview line:

HTML splitting preserves semantic structure of web documents for RAG ingestion.

---

## Structure-Based Splitting Summary

Structure-based splitting follows document hierarchy instead of character length.

This improves semantic integrity and retrieval accuracy.

Use when document structure matters more than chunk size.


---

## Chunk Size Tradeoffs

Too large:
- noisy retrieval
- mixed topics

Too small:
- lost context
- incomplete answers

Balanced chunking is critical.

Typical production values:

chunk_size: 300–800
chunk_overlap: 30–100

---

## load vs split_documents

load() → creates documents  
split_documents() → creates chunks

Documents = original data  
Chunks = retrievable units

---

## Interview Key Points

- Text splitting is required for RAG scalability
- RecursiveCharacterTextSplitter is the default choice
- Semantic splitting preserves conceptual coherence
- Overlap prevents context loss
- Chunk size tuning affects retrieval accuracy
- Metadata preservation enables citation systems

---

## 20-Second Interview Summary

Text splitters break large documents into smaller semantic chunks,
balancing context preservation and retrieval accuracy.
Proper chunking directly impacts RAG performance.

---

## Quick Cheat Sheet

Recursive splitter → general use  
Markdown splitter → structured docs  
HTML splitter → websites  
Semantic splitter → meaning-based chunking  

chunk_size = chunk length  
chunk_overlap = shared context  

Good splitting = good RAG

