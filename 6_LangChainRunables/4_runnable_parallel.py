"""
Requirements - You must create:

1️⃣ Joke chain
Prompt: Tell a funny joke about {topic}

2️⃣ Tweet chain
Prompt: Write a short viral tweet about {topic}

3️⃣ Fact chain
Prompt: Give an interesting fact about {topic}

Rules
✅ Use RunnableParallel
✅ Each chain must use:

Prompt → model → StrOutputParser

"""

from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-4.7",
    task='text-generation'
)
model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

# prompt 1
joke_prompt = PromptTemplate(
    template = "Tell a funny joke about {topic}",
    input_variables=["topic"]
)
# prompt 2
tweet_prompt = PromptTemplate(
    template="Write a short viral tweet about {topic}",
    input_variables=["topic"]
)
#prompt 3 
fact_prompt = PromptTemplate(
    template="Give an interesting fact about {topic}",
    input_variables=["topic"]
)

joke_chain = joke_prompt | model | parser
tweet_chain = tweet_prompt | model | parser
fact_chain = fact_prompt | model | parser

parallel_chain = RunnableParallel({
    "joke" : joke_chain,
    "tweet" : tweet_chain,
    "fact" : fact_chain
})

response = parallel_chain.invoke({'topic':'AI'})

print(response["joke"])
print(response["tweet"])
print(response["fact"])


"""
RunnableParallel automatically returns a Python dictionary, 
which looks like JSON when printed, even though StrOutputParser only returns plain text.

# RunnableParallel
# Runs multiple branches at same time
# Same input sent to all branches
# Returns dictionary of branch outputs
# Example return: {"joke": "...", "fact": "..."}
# Mental model: fan-out execution

"""