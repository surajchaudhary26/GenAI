"""
RunnableLambda Challenge

Generate a joke
👉 then count how many words are in the joke
👉 return both joke + word count

Expected output shape
{
  "joke": "...",
  "word_count": 23
}
Requirements - 
 - create joke chain (Prompt → model → parser)
 - use RunnableLambda to count words
 - use RunnableParallel to return both outputs
"""
## we'll address issue of "5_runnable_passthrough.py" here
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-4.7",
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

prompt = PromptTemplate.from_template(
    "Tell a short funny joke about {topic}"
)

joke_chain = prompt | model | parser

def count_words(text):
    return len(text.split())

parallel_chain = RunnableParallel({
    "joke": joke_chain,
    "word_count": joke_chain | RunnableLambda(count_words)
})

response = parallel_chain.invoke({"topic": "AI engineers"})
print(response)

"""
# RunnableLambda
# Wraps a Python function
# Returns whatever the function returns
# Can return string / number / dict / anything
# Used for transformation or reshaping
# Mental model: data transformer node

"""