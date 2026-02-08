from langchain_core.runnables import RunnableLambda

def add_one(num):
    return num+1;
runnable1 = RunnableLambda(add_one)

def multiply_two(num):
    return num*2
runnable2 = RunnableLambda(multiply_two)

chain = runnable1 | runnable2

response = chain.invoke(5)
print(response)


"""
What happened

Execution flow:
5
→ add_one → 6
→ multiply_two → 12


That | operator is RunnableSequence.
You just built your first pipeline.
No LLM. Just data flow.

This is exactly how LangChain chains prompts and models."""