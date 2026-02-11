from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text = """
Farmers were working hard in the fields, preparing soil and planting seeds. The weather was warm and the smell of fresh earth filled the air. Agriculture requires patience, planning, and understanding of nature. Many rural families depend entirely on farming for survival.

The Indian Premier League is one of the largest cricket leagues in the world. Millions of fans watch the matches every season. Teams compete fiercely and players become international stars. Cricket brings entertainment and unity to people across countries.

Terrorism is a serious threat to global peace. Attacks create fear and destroy communities. Governments invest heavily in security to protect citizens. International cooperation is necessary to fight extremist violence.

"""

# Gemini embeddings (free tier)
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)


docs = splitter.create_documents([text])

for i, doc in enumerate(docs):
    print(f"\nChunk {i+1}:")
    print(doc.page_content)
