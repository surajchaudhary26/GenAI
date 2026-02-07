from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# HuggingFace model
llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-4.7",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)


detail_report = PromptTemplate(
    template="Write a detailed report about {topic}",
    input_variables=["topic"],    
)

summery_report = PromptTemplate(
    template="Summarize the following report in 5 bullet points:\n{report}",
    input_variables=["report"]
)
parser = StrOutputParser()

chain = detail_report | model | summery_report | model | parser

response = chain.invoke({"topic":"photo synthesis"})
print(response)


"""
topic
 ↓
report generation
 ↓
summary generation
 ↓
clean text output
"""