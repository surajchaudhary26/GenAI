from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

""" Using open-source model through api from Hugging face 
steps: 
    - go to hugging face website 
    - Select the Task 
    - click on model 
    - copy repo-id from top left side 
"""

load_dotenv()

# Step 1: Create HuggingFace endpoint
llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-4.7",
    task="text-generation"
)


# Step 2: Wrap into Chat model
chatModel = ChatHuggingFace(llm=llm)

# Step 3: Invoke
response = chatModel.invoke("Name three fruits")
print(response.content)
