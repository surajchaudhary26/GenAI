from langchain_core.runnables import RunnableLambda

def add_one(x):
    return x + 1

# convert into Runnable
runnable = RunnableLambda(add_one)

result = runnable.invoke(5)

print(result)

"""
Turn a normal Python function into a Runnable.

Now it behaves like:
- LLM
- prompt
- Parser
- retriever

Everything in LangChain is treated the same way.
"""