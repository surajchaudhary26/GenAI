from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

# HuggingFace model
llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-4.7",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

# Prompt 1 → notes generator
notes_prompt = PromptTemplate(
    template="Create study notes from the following text:\n{text}",
    input_variables=["text"]
)

# Prompt 2 → quiz generator
quiz_prompt = PromptTemplate(
    template="Create 3 quiz questions from the following text:\n{text}",
    input_variables=["text"]
)

parser = StrOutputParser()

# Parallel chain
parallel_chain = RunnableParallel(
    notes = notes_prompt | model | parser,
    quiz = quiz_prompt | model | parser
)

text = """
Big Bang theory
"""

result = parallel_chain.invoke({"text": text})

print(result)