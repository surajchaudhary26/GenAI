from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me Hardik pandeya'

emedding_model = GoogleGenerativeAIEmbeddings(
    model = 'gemini-embedding-001',
    output_dimensionality=32
)
# Embedding documnet
documents_vec = emedding_model.embed_documents(documents)

# Embedding query
query_vec = emedding_model.embed_query(query)

# cosine similarity
scores = cosine_similarity(documents_vec, [query_vec])
print(scores)

# Flatten into 1D array
scores = scores.flatten() 

# Return index of max value 
index = np.argmax(scores)

# Get the best score 
score = scores[index]

print(query)
print(documents[index])
print("similarity score is:", score)