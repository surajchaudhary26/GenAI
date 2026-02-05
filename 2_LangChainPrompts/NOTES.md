# LangChain Prompt Components — Notes

## 1. Static vs Dynamic Prompts

### Static Prompt

A static prompt is a fixed string that never changes.

Example:

```python
prompt = "Summarize this research paper."
```

Use when:
- No user input is required
- Same instruction every time
- Testing or debugging

Pros:
- Simple
- Predictable output

Cons:
- Not flexible
- Cannot adapt to user inputs

---

### Dynamic Prompt

A dynamic prompt uses variables that change at runtime.

LangChain supports dynamic prompts using `PromptTemplate`.

Example:

```python
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="Summarize {topic} in {style} style",
    input_variables=["topic", "style"]
)

prompt = template.invoke({
    "topic": "Transformers",
    "style": "simple"
})
```

Use when:
- User provides inputs
- Prompt must adapt
- Building apps/chatbots

Key idea:
> Dynamic prompts = reusable + parameterized instructions

---

## 2. Message Types in LangChain

LangChain chat models use structured message roles.

Each message has a **type** and **content**.

### System Message

Controls behavior of the AI.

Example:

```python
SystemMessage("You are a helpful research assistant.")
```

Purpose:
- Sets personality
- Defines rules
- Controls tone

Think of it as:
> Global instructions

---

### Human Message

Represents user input.

```python
HumanMessage("Explain neural networks.")
```

Purpose:
- Actual question or request
- Dynamic user content

---

### AI Message

Represents model output.

```python
AIMessage("Neural networks are...")
```

Used to:
- Store history
- Build memory
- Continue conversation

---

### Message Flow

```
System → Human → AI → Human → AI ...
```

This structure enables:
- Chat memory
- Context awareness
- Multi-turn conversations

---

## 3. ChatPromptTemplate

`ChatPromptTemplate` builds structured chat prompts using messages.

It’s used instead of plain string prompts for chat models.

Example:

```python
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert teacher."),
    ("human", "Explain {topic} simply.")
])

prompt = chat_template.invoke({"topic": "Machine Learning"})
```

Output becomes:

System: You are an expert teacher.
Human: Explain Machine Learning simply.

Benefits:
- Clean structure
- Role-based prompts
- Easy conversation design

Use when:
- Building chatbots
- Using GPT-style models
- Multi-message prompts

---

## 4. Message Placeholder

A message placeholder allows inserting dynamic conversation history.

Useful for chat memory.

Example:

```python
from langchain_core.prompts import MessagesPlaceholder

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a tutor."),
    MessagesPlaceholder("history"),
    ("human", "{question}")
])
```

Then:

```python
chat_template.invoke({
    "history": previous_messages,
    "question": "Explain recursion"
})
```

Purpose:
- Inject chat history
- Maintain context
- Continue conversations naturally

Without placeholders:
→ Model forgets past messages

With placeholders:
→ Model remembers conversation

---

## Mental Model Summary

```
Static prompt → fixed string

Dynamic prompt → PromptTemplate with variables

ChatPromptTemplate → structured multi-message prompt

Message types → system / human / AI roles

MessagesPlaceholder → inject memory/history
```

---

## When to Use What

Static prompt:
→ Simple one-shot tasks

Dynamic prompt:
→ User-driven apps

ChatPromptTemplate:
→ Chatbots & assistants

Message placeholder:
→ Memory & conversation continuity

---

## Interview Key Points

- PromptTemplate enables reusable dynamic prompts
- ChatPromptTemplate organizes role-based conversations
- System message controls AI behavior
- MessagesPlaceholder enables chat memory
- LangChain prompts are composable and chainable

---

## Quick Best Practices

- Always use dynamic prompts for apps
- Use system message to define tone
- Keep prompts explicit and structured
- Avoid ambiguity
- Use placeholders for memory-enabled agents

---

---

## 5. Why Use PromptTemplate Instead of f-strings?

You *can* build prompts using Python f-strings:

```python
topic = "Transformers"
prompt = f"Explain {topic} simply."
```

But in production LangChain apps, `PromptTemplate` is better.

---

### Problems with f-strings

❌ Not reusable  
Each prompt is manually written

❌ No input validation  
If a variable is missing → runtime crash

❌ Hard to scale  
Messy when prompts grow large

❌ No integration with LangChain chains  
Cannot easily plug into pipelines

❌ No template safety checks  
Typos go unnoticed

---

### Benefits of PromptTemplate

```python
template = PromptTemplate(
    template="Explain {topic} simply.",
    input_variables=["topic"]
)
```

✅ Reusable prompt structure  
Write once, use everywhere

✅ Variable validation  
LangChain checks missing inputs

✅ Safer prompt construction  
Prevents formatting mistakes

✅ Works natively with chains

```
template | model
```

✅ Serializable (can save as JSON)  
Important for production systems

```
template.save("template.json")
```

✅ Easier collaboration  
Teams can share templates

---

### Mental Model

```
f-string → quick script
PromptTemplate → production system
```

Use f-strings for:
- Small experiments
- Quick tests

Use PromptTemplate for:
- Real applications
- Chatbots
- APIs
- Agents
- RAG pipelines

---

### Interview Answer (Short Version)

> PromptTemplate is safer, reusable, validated, and integrates directly with LangChain chains. f-strings are fine for quick scripts, but PromptTemplate is designed for scalable production workflows.

---

End of Section
