# LangChain Output Parsers — Notes

## Core Idea

LLMs return messy human text.

Applications need structured machine-readable data.

Output Parsers convert:

```
LLM text → structured result
```

This enables integration with:
- APIs
- databases
- automation pipelines
- agents
- dashboards

---

## Why Output Parsers Exist

Raw LLM response:

```
"The sentiment seems positive overall..."
```

Structured output needed:

```json
{"sentiment": "pos"}
```

Parsers act as translators between human text and system data.

---

## 1. String Output Parser

### Purpose

Extracts only the text content from the LLM response.

Removes message wrappers.

### Example

```python
from langchain_core.output_parsers import StrOutputParser

chain = model | StrOutputParser()
result = chain.invoke("Say hello")
```

Output:

```
"Hello"
```

### Use cases

- clean text pipelines
- streaming
- chaining LLM steps
- removing metadata

Think:

> keep text, discard wrapper

---

## 2. JSON Output Parser

### Purpose

Forces model to return JSON format.

### Example

```python
from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser()
chain = model | parser
```

Output:

```json
{"name": "Suraj", "age": 23}
```

### Limitations

- no strict schema enforcement
- model decides structure
- no type validation

Use when:

- quick prototypes
- loose JSON extraction
- experiments

---

## 3. Structured Output Parser

### Purpose

Allows defining a fixed JSON schema.

Model must follow structure.

### Features

- predictable keys
- controlled shape
- no deep validation

Think:

> structured format without strict validation

Use when:

- stable schema needed
- light safety is enough

---

## 4. Pydantic Output Parser ⭐

### Purpose

Strict schema + runtime validation.

Production-grade parser.

### Example

```python
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
```

If model returns wrong type:

```
age = "twenty"
```

Parser raises error.

### Benefits

- strict type safety
- schema enforcement
- data validation
- safe automation
- DB-ready objects

Use when:

- production systems
- APIs
- finance/healthcare
- reliable pipelines

---

## Parser Comparison

| Parser | Structure | Validation | Safety | Use case |
|--------|----------|------------|--------|---------|
String | ❌ | ❌ | Low | raw text |
JSON | Loose | ❌ | Medium | quick JSON |
Structured | Fixed shape | ❌ | Medium | controlled schema |
Pydantic | Strict | ✅ | High | production apps |

---

## Important Insight

Output parsers are model-agnostic.

They work with:

- OpenAI models
- Gemini
- open-source LLMs
- local models

They standardize output regardless of LLM.

---

## Mental Model

```
LLM = creative writer
Parser = strict accountant
```

Writer generates text.
Parser formats it into usable data.

---

## When to Use What

Small chatbot → String parser  
Prototype → JSON parser  
Controlled app → Structured parser  
Real product → Pydantic parser

---

## Interview Explanation

Output parsers convert unstructured LLM responses into structured, machine-readable formats such as JSON or validated objects, enabling safe integration into real-world systems.

---

## Key Takeaway

LLMs generate text.

Applications need data.

Output parsers bridge the gap.

---

End of Notes
