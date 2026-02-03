from langchain_huggingface import HuggingFaceEmbeddings
import sentence_transformers

"""
This is an open-source embedding model from Hugging Face.
    👉 It runs on your machine
    👉 No API key
    👉 No cost
    👉 No internet after download
"""
hf_embedding_model = HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-MiniLM-L6-v2'
    )

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

response_vec = hf_embedding_model.embed_documents(documents)

print(str(response_vec))