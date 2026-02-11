from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

from dotenv import load_dotenv

load_dotenv()

# embedding model
# embeddings = OpenAIEmbeddings()
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

# create vector store
vector_store = Chroma(
    collection_name="ipl_players",
    embedding_function=embeddings,
    persist_directory="7_RAG/3_vectorStore/chroma_db"
)

# AI + Sports + Health mixed dataset

docs = [
    Document(
        page_content="Artificial Intelligence allows machines to simulate human intelligence. It is used in chatbots, self-driving cars, and recommendation systems.",
        metadata={"category": "AI"}
    ),
    Document(
        page_content="Machine learning is a subset of AI that enables systems to learn from data without explicit programming.",
        metadata={"category": "AI"}
    ),
    Document(
        page_content="Deep learning uses neural networks with many layers to solve complex problems like image recognition and speech processing.",
        metadata={"category": "AI"}
    ),
    Document(
        page_content="Cricket is one of the most popular sports in the world, especially in India and Australia.",
        metadata={"category": "Sports"}
    ),
    Document(
        page_content="Football is played by millions globally and major tournaments like the FIFA World Cup attract huge audiences.",
        metadata={"category": "Sports"}
    ),
    Document(
        page_content="Regular exercise improves cardiovascular health and reduces stress.",
        metadata={"category": "Health"}
    ),
    Document(
        page_content="A balanced diet with proteins, vitamins, and minerals is essential for good health.",
        metadata={"category": "Health"}
    ),
]


# add documents only if it is empty
if len(vector_store.get()["ids"]) == 0:
    vector_store.add_documents(docs)

# Alternative if overWrite previous data
"""

vector_store.add_documents(
    docs,
    ids=["ai1","ai2","ai3","sports1","sports2","health1","health2"]
)
"""

# view stored data
data = vector_store.get(include=["documents", "metadatas"])
# print(data)

results = vector_store.similarity_search("How do machines learn?")
# results = vector_store.similarity_search("popular global sport")
# results = vector_store.similarity_search("how to stay healthy")


for r in results:
    print("\nResult:", r)
