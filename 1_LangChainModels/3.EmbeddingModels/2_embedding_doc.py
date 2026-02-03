from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

emedding_model = GoogleGenerativeAIEmbeddings(
    model = 'gemini-embedding-001',
    output_dimensionality=32
)

response_vec = emedding_model.embed_documents(documents)  
print(response_vec)