from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# same embedding model
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

# connect to existing DB
vector_store = Chroma(
    collection_name="ipl_players",
    embedding_function=embeddings,
    persist_directory="7_RAG/3_vectorStore/chroma_db"
)

# 1️⃣ view stored data
data = vector_store.get(
        include=["documents", "metadatas"]
    )
print("\nStored Data:", data)
# print("\nGet Ids : ", vector_store.get(include=["id"])) 

# # 2️⃣ similarity search
# results = vector_store.similarity_search("How do machines learn?")

# for r in results:
#     print("\nSearch Result:", r.page_content)

# # 3️⃣ filter by metadata
# sports = vector_store.similarity_search(
#     "popular sport",
#     filter={"category": "Sports"}
# )

# for r in sports:
#     print("\nFiltered Result:", r.page_content)

"""
text → embedding
embedding → vector DB
vector DB → nearest match
match → document return

"""