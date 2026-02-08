# LangChain Runnables — Complete Notes

## Overview

LangChain Runnables are the foundational abstraction that standardize how components interact inside LangChain. They transform LangChain from a loose collection of tools into a composable AI workflow framework.

A Runnable represents a unit of computation:

input → processing → output

Every major LangChain component — prompts, LLMs, retrievers, parsers, and tools — is implemented as a Runnable. Because they share a unified interface, they can be connected seamlessly like Lego blocks.

Understanding Runnables means understanding LangChain architecture.

---

## Why Runnables Exist

Early LangChain suffered from architectural problems:

- Too many custom chain classes
- No unified interface
- Inconsistent input/output formats
- High learning curve
- Hard workflow composition
- Excess boilerplate code

Engineers often needed to write custom chains even for simple pipelines.

Runnables were introduced to:

- standardize execution
- remove custom chain boilerplate
- enable composable workflows
- support streaming and batching
- allow graph-style execution
- simplify developer experience

Runnables turned LangChain into a dataflow programming framework.

Instead of scripting prompts, developers wire computation graphs.

---

## Core Runnable Interface

Every Runnable follows the same contract:

.invoke(input) → output  
.batch(list_of_inputs) → list_of_outputs  
.stream(input) → streaming output  

This guarantees interoperability.

Any component implementing this interface can be inserted anywhere in a pipeline.

This is the key to modular architecture.

---

## Runnable Categories

### Task-Specific Runnables

These perform actual AI tasks:

- ChatOpenAI / LLM models
- PromptTemplate
- OutputParser
- Retriever
- Memory modules
- Tools
- Embedding models

They generate or process data.

### Runnable Primitives

These control workflow logic:

- sequencing
- parallel execution
- branching
- routing
- transformation
- data preservation

They orchestrate pipelines.

Think:

Task Runnables = workers  
Runnable Primitives = managers

---

## Runnable Primitives

Runnable primitives define how Runnables connect and execute.

They form the wiring layer of LangChain.

---

### RunnableSequence

Executes Runnables sequentially.

Output of one becomes input to the next.

A → B → C

Code:

```python
chain = A | B | C
```

Equivalent execution:

```python
output = C(B(A(input)))
```

Use cases:

- prompt → LLM → parser
- retriever → formatter → LLM
- multi-step reasoning
- RAG pipelines

Mental model: assembly line.

---

### RunnableParallel

Executes multiple Runnables in parallel with the same input.

        → A →
input →        → merge results
        → B →
        → C →

Code:

```python
parallel = RunnableParallel({
    "tweet": tweet_chain,
    "linkedin": linkedin_chain
})
```

Output:

```python
{
  "tweet": "...",
  "linkedin": "..."
}
```

Use cases:

- multi-format generation
- ensemble prompting
- redundancy systems
- multi-perspective reasoning
- evaluation pipelines

Mental model: fan-out execution.

---

### RunnablePassthrough

Returns input unchanged.

Identity function:

f(x) = x

Code:

```python
RunnablePassthrough()
```

Purpose:

Preserve original input while processing branches.

Example:

```python
RunnableParallel({
    "original": RunnablePassthrough(),
    "processed": chain
})
```

Use cases:

- preserving raw input
- metadata forwarding
- combining original + processed output
- routing context downstream

Mental model: identity wire.

---

### RunnableLambda

Wraps any Python function into a Runnable.

Code:

```python
def word_count(text):
    return len(text.split())

count = RunnableLambda(word_count)
```

This bridges LangChain and regular Python logic.

Use cases:

- custom validation
- transformation logic
- logging
- filtering
- analytics
- database writes
- metrics collection
- business rules

Mental model: adapter layer.

Injects arbitrary Python logic into pipelines.

---

### RunnableBranch

Conditional execution.

Acts like an if/else statement.

if condition:
    A
else:
    B

Code:

```python
branch = RunnableBranch(
    (condition, long_chain),
    short_chain
)
```

Use cases:

- summarization triggers
- safety filters
- guardrails
- adaptive routing
- threshold-based decisions
- dynamic workflows

Mental model: decision tree node.

Introduces logic into pipelines.

---

## LangChain Expression Language (LCEL)

LCEL is a declarative syntax for composing Runnable pipelines.

Before:

```python
RunnableSequence([A, B, C])
```

With LCEL:

```python
A | B | C
```

Benefits:

- concise syntax
- readable pipelines
- less boilerplate
- mirrors mental model
- easier debugging

LCEL expresses computation graphs directly in code.

It is both syntax sugar and design philosophy.

---

## Dataflow Architecture

LangChain pipelines are computation graphs.

Nodes = Runnables  
Edges = data flow

Example graph:

input  
 → retriever  
 → formatter  
 → prompt  
 → llm  
 → parser  
 → output  

This architecture is similar to:

- TensorFlow graphs
- Apache Airflow DAGs
- Unix pipes
- functional pipelines

LangChain is evolving into workflow orchestration.

You are wiring systems, not scripting prompts.

---

## Real RAG Example

```python
rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | parser
)
```

Execution flow:

1. Retriever fetches documents
2. Question preserved via passthrough
3. Prompt merges context + question
4. LLM generates answer
5. Parser formats output

No custom chain classes required.

Everything is composable.

---

## Streaming and Batch Support

Because all components follow the Runnable interface:

Streaming:

```python
chain.stream(input)
```

Batch processing:

```python
chain.batch([input1, input2])
```

Streaming and batching automatically propagate through pipelines.

This is critical for production systems.

---

## Advantages of Runnable Architecture

- composability
- modular design
- standardized interface
- streaming support
- batch execution
- parallel processing
- conditional routing
- Python integration
- graph-style workflows
- scalability
- reduced boilerplate
- production readiness

Runnables make LangChain extensible and future-proof.

---

## Interview Explanation

Runnables are a standardized abstraction in LangChain that treat prompts, models, retrievers, and custom logic as nodes in a computation graph. Runnable primitives enable sequential, parallel, and conditional composition, while LCEL provides a declarative syntax to build pipelines. This turns LangChain into a dataflow orchestration framework rather than a simple LLM wrapper.

---

## Mental Model Summary

LangChain is an AI workflow engine.

Runnables = computation nodes  
Primitives = wiring logic  
LCEL = pipeline language  

You are building graphs, not scripts.

---

## Advanced Insight

Runnables are the foundation of:

- LangGraph agent systems
- multi-agent orchestration
- tool calling pipelines
- streaming architectures
- evaluation frameworks
- production LLM systems

Everything advanced in LangChain builds on Runnables.

Understanding them means understanding modern AI system design.

---

## Final Takeaway

If you understand Runnables, you understand LangChain.

They shift development from prompt scripting to workflow engineering.

That is the future of AI application architecture.
