from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

# Embedding model
embedding_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

# Documents
all_docs = [
    Document(page_content="Regular walking boosts heart health and energy.", metadata={"source": "H1"}),
    Document(page_content="Fruits and vegetables improve metabolism and vitality.", metadata={"source": "H2"}),
    Document(page_content="Deep sleep restores mental and physical energy.", metadata={"source": "H3"}),
    Document(page_content="Mindfulness reduces stress and increases focus.", metadata={"source": "H4"}),
    Document(page_content="Drinking water supports energy balance.", metadata={"source": "H5"}),
]

# LLM for query expansion
llm = ChatGoogleGenerativeAI(model="gemini-flash-lite-latest")

# Vector DB
vectorstore = Chroma.from_documents(all_docs, embedding_model)

query = "How to improve energy levels and maintain balance?"

# Step 1 — Generate alternative queries
prompt = f"Generate 4 alternative search queries for: {query}"
response = llm.invoke(prompt)

queries = [q.strip() for q in response.content.split("\n") if q.strip()]

print("\nGenerated Queries:")
for q in queries:
    print("-", q)

# Step 2 — Retrieve docs for each query
docs = []
for q in queries:
    docs.extend(vectorstore.similarity_search(q, k=1))

# Remove duplicates
unique_docs = list({doc.page_content: doc for doc in docs}.values())

print("\nMulti-Query Results:")
for d in unique_docs:
    print("-", d.page_content)
