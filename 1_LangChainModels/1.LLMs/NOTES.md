# LangChain Models: LLM vs ChatModel

## Introduction

LangChain provides two main abstractions to interact with language models:

1. **LLM (Text Completion Model)**
2. **ChatModel (Chat Completion Model)**

Both represent ways to communicate with large language models, but they differ in how they accept input, manage context, and produce output.

Understanding this distinction is fundamental for building modern GenAI systems such as chatbots, RAG pipelines, and AI agents.

---

## Section 1: LLM (Text Completion Model)

### Definition

An **LLM** in LangChain is a model that takes plain text input and returns plain text output.

```
Input: string
Output: string
```

It does not understand conversation roles or structured messages. It behaves like an advanced text auto-completion engine.

---

### Mental Model

**LLM = advanced autocomplete system**

You give a prompt, and the model continues it.

```
Prompt → Model → Text Completion
```

There is no built-in notion of:

- system instructions
- conversation roles
- chat memory
- multi-turn dialogue

Everything must be manually embedded inside a single string.

---

### Example (Concept)

Input:
```
Explain recursion simply.
```

Output:
```
Recursion is a technique where a function calls itself...
```

---

### LangChain Example

```python
from langchain_openai import OpenAI

llm = OpenAI(model="gpt-3.5-turbo-instruct")
result = llm.invoke("Explain recursion simply")
print(result)
```

---

### Characteristics of LLM

- Works with raw strings
- Stateless by default
- No built-in conversation awareness
- Simpler abstraction
- Good for single-shot tasks

---

### Typical Use Cases

- Text summarization
- Translation
- Data extraction
- Classification
- Code generation
- Document transformation
- Backend automation pipelines

LLMs are useful when you only need a single input-output transformation.

---

### Limitations of LLM

- Cannot naturally handle conversation
- No role separation (system/user/assistant)
- Hard to maintain memory
- Weaker instruction control
- Less safe and less aligned than chat models

They are considered a legacy-style interface compared to chat models.