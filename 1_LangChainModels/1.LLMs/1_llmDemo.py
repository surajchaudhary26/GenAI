from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct') # Choose LLM
response = llm.invoke("Who is prime minister of india?")
print(response)