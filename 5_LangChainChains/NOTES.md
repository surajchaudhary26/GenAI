# LangChain Chains — Notes

## Core Idea

A chain is a pipeline where:

```
output of step A → input of step B
```

Chains automate multi-step LLM workflows.

Instead of manually calling models again and again, chains connect components into a flow.

---

## Why Chains Exist

Without chains:

- manual model calls
- messy code
- repeated extraction
- hard to scale

With chains:

- clean pipeline
- automatic data passing
- reusable architecture
- production-ready workflows

Think:

```
function composition for LLMs
```

---

## Basic Chain

Simplest chain:

```
Prompt → Model → Output Parser
```

Example:

```python
chain = prompt | model | parser
result = chain.invoke({"topic": "black hole"})
```

LangChain automatically passes outputs between steps.

---

## Sequential Chain

Sequential chain = multi-step pipeline.

Example flow:

```
topic → detailed report → summary
```

Step 1: generate report  
Step 2: summarize report

```
prompt1 | model | prompt2 | model
```

Each step uses previous output.

Use case:

- report generation
- research pipelines
- document summarization
- multi-stage reasoning

---

## Parallel Chain

Parallel chains run multiple tasks at the same time.

Built using:

```
RunnableParallel
```

Example:

```
text → notes generator
     → quiz generator
```

Both run simultaneously.

Output:

```
{
  "notes": "...",
  "quiz": "..."
}
```

Use case:

- generate multiple artifacts
- dashboards
- education tools
- content pipelines

Parallel = faster + efficient

---

## Conditional Chain

Conditional chains branch logic based on conditions.

Built using:

```
RunnableBranch
```

Example:

```
feedback → sentiment classifier
          → positive chain
          → negative chain
```

System chooses path automatically.

Use case:

- chat routing
- customer support
- decision trees
- moderation pipelines

Think:

```
if/else for LLM workflows
```

---

## RunnableLambda

RunnableLambda converts normal Python functions into chain-compatible steps.

Example:

```python
RunnableLambda(lambda x: x.upper())
```

This allows custom logic inside chains.

Use case:

- preprocessing
- formatting
- filtering
- transformation

---

## Mental Model

```
Chains = LLM workflow engine
```

They connect:

- prompts
- models
- parsers
- functions
- memory
- tools

into a single pipeline.

---

## Types of Chains Summary

| Chain Type | Purpose |
|-----------|--------|
Basic | single pipeline |
Sequential | multi-step workflow |
Parallel | simultaneous execution |
Conditional | decision-based routing |

---

## Key Takeaway

Chains remove manual glue code.

They turn LLM calls into structured pipelines.

Essential for real AI applications.

---

## 1-line Interview Answer

Chains in LangChain allow building automated multi-step LLM workflows by connecting prompts, models, and parsers into composable pipelines.

---

End of Notes
