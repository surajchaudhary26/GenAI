from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
# Step 1: Embedding model 
embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

# Step 2: Sample documents

documents = [
    Document(
        page_content="Artificial Intelligence enables machines to simulate human thinking and decision-making.",
        metadata={"category": "AI", "source": "ai_intro"}
    ),
    Document(
        page_content="Machine learning is a subset of AI where systems learn patterns from data automatically.",
        metadata={"category": "AI", "source": "ml_basics"}
    ),
    Document(
        page_content="Deep learning uses multi-layer neural networks to solve complex problems like image recognition.",
        metadata={"category": "AI", "source": "deep_learning"}
    ),
    Document(
        page_content="Cricket is one of the most popular sports worldwide, especially in India and Australia.",
        metadata={"category": "Sports", "source": "cricket_info"}
    ),
    Document(
        page_content="Football tournaments like the FIFA World Cup attract millions of viewers globally.",
        metadata={"category": "Sports", "source": "football_info"}
    ),
    Document(
        page_content="Regular exercise improves heart health and reduces mental stress.",
        metadata={"category": "Health", "source": "fitness_guide"}
    ),
    Document(
        page_content="A balanced diet rich in vitamins and proteins is essential for long-term health.",
        metadata={"category": "Health", "source": "nutrition_guide"}
    ),
]



# Step 3: Create Chroma vector store in memory

"""
    It never gets saved to folder. Since we have not specified the directory 
    {persist_directory="./chroma_db"}
    Without persist_directory, Chroma runs in memory. With persist_directory, 
    it creates a persistent on-disk vector database.

"""
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="my_collection"
)

# Step 4: Convert vectorstore into a retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

query = "What is artificial intelligence?"

''' QUERIES : 
    
    "How do machines learn from data?"
    "What is artificial intelligence?"
    "Explain neural networks"

    "Which sport is popular in India?"
    "Tell me about football tournaments"
    "global sports audience"

    "Which sport is popular in India?"
    "Tell me about football tournaments"
    "global sports audience"

'''


results = retriever.invoke(query)
for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)


results = vectorstore.similarity_search(query, k=2)
for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)

"""
| Retriever             | similarity_search |
| --------------------- | ----------------- |
| high-level interface  | low-level DB call |
| supports strategies   | basic search only |
| chain compatible      | manual use        |
| future-proof          | tightly coupled   |
| used in RAG pipelines | debugging/demo    |

"""