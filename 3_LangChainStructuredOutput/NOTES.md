---

## 6. Structured Output in LangChain

Structured output means forcing the LLM to return data in a predictable format like:

- JSON
- Dictionary
- List
- Pydantic object
- Typed schema

Instead of free text:

❌ "The answer is probably 42"

We want:

✅ `{ "answer": 42 }`

Structured output is critical for:

- APIs
- Automation
- Data pipelines
- Agents
- UI apps
- Tool calling

---

## Why Structured Output Matters

LLMs normally generate text.

But production systems need:

- machine-readable output
- consistent format
- validation
- error handling

Structured output makes LLM responses programmable.

---

## Method 1: Output Parser

LangChain uses Output Parsers to convert text → structured data.

Example: JSON Output Parser

```python
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI

parser = JsonOutputParser()

chain = model | parser
result = chain.invoke("Give a JSON with name and age")
```

Output:

```json
{
  "name": "Alice",
  "age": 25
}
```

The parser ensures valid JSON.

---

## Method 2: Pydantic Output Parser

Best for typed, validated outputs.

```python
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser

class Person(BaseModel):
    name: str
    age: int

parser = PydanticOutputParser(pydantic_object=Person)
```

Now the model must return:

```
Person(name="Alice", age=25)
```

Benefits:

✅ Type safety  
✅ Validation  
✅ Clear schema  
✅ Production ready

---

## Method 3: Structured Prompt + Format Instructions

Parser can inject format instructions into prompt:

```python
format_instructions = parser.get_format_instructions()

prompt = PromptTemplate(
    template="Extract info.\n{format_instructions}\n{text}",
    input_variables=["text"],
    partial_variables={"format_instructions": format_instructions}
)
```

This tells the LLM exactly how to format output.

---

## Method 4: Tool / Function Calling (Modern Approach)

Some models support native structured output:

- OpenAI function calling
- JSON schema enforcement

LangChain integrates this automatically.

Example:

```python
structured_model = model.with_structured_output(Person)
result = structured_model.invoke("Alice is 25")
```

No parsing needed — model returns validated object.

This is the most reliable method.

---

## Mental Model

```
LLM text → parser → structured object
```

or

```
LLM → native schema → structured object
```

---

## When to Use Structured Output

Use it when:

- building APIs
- storing data in DB
- automation workflows
- agents calling tools
- UI apps expecting JSON
- extracting fields from text

Avoid free text in production systems.

---

## Best Practices

- Prefer Pydantic schema
- Validate outputs
- Give clear format instructions
- Keep schema simple
- Handle parsing errors

---

## Interview Key Points

- Structured output ensures machine-readable responses
- Output parsers convert text to typed objects
- Pydantic parser provides validation
- Modern models support native structured output
- Essential for production LangChain apps

---

## Short Interview Answer

> Structured output forces LLM responses into validated schemas like JSON or Pydantic models, making outputs reliable, machine-readable, and safe for automation.

---

End of Section
