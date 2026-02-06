# Import Gemini chat model from LangChain Google integration
from langchain_google_genai import ChatGoogleGenerativeAI

# Loads environment variables from .env file (API keys etc.)
from dotenv import load_dotenv

# TypedDict helps define structured schema for LLM output
# Annotated adds instructions to guide the model
# Optional means the field can be missing
# Literal restricts values to specific choices
from typing import TypedDict, Annotated, Optional, Literal


# Load API key from .env into environment
# Without this → model authentication fails
load_dotenv()


# Initialize Gemini model
# This is the LLM we will call
model = ChatGoogleGenerativeAI(model="gemini-flash-lite-latest")


# -------------------------------
# STRUCTURED OUTPUT SCHEMA
# -------------------------------

# TypedDict defines a strict structure the LLM must follow
# Think of this like a JSON schema or contract

class Review(TypedDict):

    # Annotated tells the model what to extract
    # list[str] means we expect a list of strings
    key_themes: Annotated[
        list[str],
        "Write down all the key themes discussed in the review in a list"
    ]

    # Short summary text
    summary: Annotated[
        str,
        "A brief summary of the review"
    ]

    # Literal restricts output to allowed values only
    sentiment: Annotated[
        Literal["pos", "neg"],
        "Return sentiment of the review either negative, positive or neutral"
    ]

    # Optional means this field can be None if missing
    pros: Annotated[
        Optional[list[str]],
        "Write down all the pros inside a list"
    ]

    cons: Annotated[
        Optional[list[str]],
        "Write down all the cons inside a list"
    ]

    name: Annotated[
        Optional[str],
        "Write the name of the reviewer"
    ]


# -------------------------------
# STRUCTURED MODEL
# -------------------------------

# with_structured_output forces the model to return a response that matches Review schema
# Instead of random text, the model MUST return structured JSON-like data

structured_model = model.with_structured_output(Review)




# Model extracts structured fields automatically

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
""")



# print(result)
# Access structured field like a dictionary since it is dict
print(result['con'])

"""
It has some issue 
    - It is not necessary that llm will respond in string only
    for example you are expecting a string in summery and llm doesn't full fill that
    it may response in any other format
    - you cannot validate your data..
    - for data validation - pydantic
"""