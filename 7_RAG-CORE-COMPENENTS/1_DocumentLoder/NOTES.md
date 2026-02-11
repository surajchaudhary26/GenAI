# LangChain Document Loaders — Interview Notes

## What is a Document Loader?

A Document Loader in LangChain is a component that imports external data (PDFs, text files, CSVs, web pages, etc.) and converts it into a standardized `Document` format.

This format allows the RAG pipeline to process data consistently.

Each loader outputs:

Document:
- page_content → actual text
- metadata → source info

---

## Why Document Loaders Matter in RAG

RAG (Retrieval Augmented Generation) requires external knowledge.

LLMs cannot directly read:
- PDFs
- CSV files
- Websites
- Databases

Document loaders act as the entry point of the RAG pipeline.

Bad ingestion → bad retrieval → bad answers.

Data quality starts at the loader stage.

---

## RAG Pipeline Overview

Raw Data
→ Document Loader
→ Text Splitter
→ Embeddings
→ Vector Database
→ Retriever
→ LLM Response

Loader is ingestion layer

---

## Common Document Loaders

### TextLoader
Used for plain text files.

Best for:
- logs
- code
- transcripts
- notes

Behavior:
Loads entire text file as documents.

---

### PyPDFLoader
Used for PDF ingestion.

Behavior:
Each PDF page becomes a separate document.

Best for:
- research papers
- books
- manuals
- reports

Limitation:
PDF formatting may break text extraction.

---

### DirectoryLoader
Loads multiple files from a folder.

Best for:
- bulk ingestion
- enterprise document sets
- large datasets

Supports file pattern filtering.

---

### WebBaseLoader
Loads content from websites.

Best for:
- blogs
- documentation pages
- static HTML sites

Not ideal for:
- JavaScript-heavy dynamic pages

---

### CSVLoader
Each CSV row becomes a document.

Best for:
- structured datasets
- product catalogs
- FAQs
- knowledge tables

---

## load() vs lazy_load()

load():
- loads everything into memory
- faster for small datasets
- risky for large corpora

lazy_load():
- streams documents one by one
- memory efficient
- preferred for production pipelines

Key difference:
eager loading vs streaming

---

## Output Format of Loaders

All loaders return:

List[Document]

Where each document contains:
- page_content
- metadata

This standardized format enables downstream processing.

---

## Custom Document Loaders

If built-in loaders are insufficient:

You can build a custom loader.

Requirement:
Return a list of Document objects.

Used for:
- APIs
- proprietary formats
- databases
- enterprise systems

---

## Interview Key Points

Strong answers should include:

- Loader = ingestion layer of RAG
- Converts raw data into structured documents
- Data quality impacts retrieval accuracy
- lazy_load preferred for large-scale systems
- Custom loaders extend LangChain flexibility

---

## 20-second RAG Explanation

RAG loads external knowledge using document loaders, splits it into chunks, embeds the chunks into a vector database, retrieves relevant context at query time, and sends it to the LLM to generate grounded answers.

---

## Quick Revision Cheat Sheet

Document Loader = data ingestion tool

TextLoader → text files  
PyPDFLoader → PDFs  
DirectoryLoader → folders  
WebBaseLoader → websites  
CSVLoader → CSV rows  

load() = eager  
lazy_load() = streaming

Output = Document objects

Loader quality = RAG quality

