from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-4.7",
    task='text-generation'

)
model = ChatHuggingFace(llm=llm)

joke_prompt = PromptTemplate(
    template="Give a joke about this {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

explain_joke = PromptTemplate(
    template="Explain the meaning of this {joke}",
    input_variables=["joke"]
)

sequence = RunnableSequence(joke_prompt| model| parser| explain_joke| model| parser)

response = sequence.invoke({'topic' : 'Ai Engineers'})
print(response)

"""
# RunnableSequence
# Runs steps sequentially (A → B → C)
# Output of one step becomes input to next
# Returns final step’s output
# Used for linear pipelines
# Mental model: assembly line

"""