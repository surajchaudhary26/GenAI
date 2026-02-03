from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

""" 
Using open-source model by downloading at our local system
"""

load_dotenv()

# Step 1: Create HuggingFace pipeline to download in you local machine
pipeline = HuggingFacePipeline.from_model_id(

    model_id="Put-your-model_id",

    task="text-generation",

    pipeline_kwargs= dict(
        tempreture = 0.5,
        max_new_token = 100
    )
)
# Step 2: Wrap into Chat model
chatModel = ChatHuggingFace(pipeline)

# Step 3: Invoke
response = chatModel.invoke("Name three fruits")
print(response.content)
