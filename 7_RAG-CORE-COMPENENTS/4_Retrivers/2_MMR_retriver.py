from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

"""
FAISS: 
 - extremely fast
 - in-memory
 - good for prototypes
 - local search

"""

load_dotenv()
# Step 1: Embedding model 
embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")


# Step 2: Sample documents

docs = [
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

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model
)

# you can try :
"""
0.3 → more diversity
0.5 → balanced
0.8 → more relevance
1.0 → almost normal search

"""
retriever = vectorstore.as_retriever(
    search_type="mmr",                          # <-- This enables MMR
    search_kwargs={"k": 3, "lambda_mult": 0.5}  # k = top results, lambda_mult = relevance-diversity balance lambda = 1 → pure relevance lambda = 0 → pure diversity
)

query = "What is artificial intelligence and how does it work?"

# Normal similarity search
normal = vectorstore.similarity_search(query, k=3)

print("\n===== NORMAL SEARCH =====")
for i, doc in enumerate(normal):
    print(f"\nResult {i+1}: {doc.page_content}")


mmr = retriever.invoke(query)

print("\n===== MMR SEARCH =====")
for i, doc in enumerate(mmr):
    print(f"\nResult {i+1}: {doc.page_content}")

## Maximum Marginal Relevance (MMR)

"""
MMR is a retrieval strategy that balances relevance and diversity.

Instead of returning the top most similar documents only,
MMR avoids redundancy by selecting results that add new information.

Key idea:
relevance ↑  redundancy ↓

Properties:
- prioritizes query relevance
- penalizes duplicate content
- encourages diverse perspectives
- controlled by lambda parameter (relevance vs diversity balance)

Interview summary:
MMR returns documents that are both relevant and non-redundant.


"""