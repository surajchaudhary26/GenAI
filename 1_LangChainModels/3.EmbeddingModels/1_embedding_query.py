from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    output_dimensionality=32
)

response_vec = embedding_model.embed_query(
    "Virat Kohli is a batsman of Indian cricket team"
)
print(response_vec)
