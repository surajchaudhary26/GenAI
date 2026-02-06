# Gemini LLM from LangChain Google integration
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional, Literal
from pydantic import BaseModel, Field
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-flash-lite-latest")

# STRUCTURED SCHEMA USING PYDANTIC
# BaseModel is Pydantic class
# This creates a strict data schema with validation

class Review(BaseModel):
    # Field() adds instructions for LLM + validation rules
    key_themes: list[str] = Field(
        description="Write down all the key themes discussed in the review in a list"
    )

    summary: str = Field(
        description="A brief summary of the review"
    )

    # Literal restricts allowed values
    sentiment: Literal["pos", "neg"] = Field(
        description="Return sentiment of the review either negative, positive or neutral"
    )

    # Optional = can be missing or None
    pros: Optional[list[str]] = Field(
        default=None,
        description="Write down all the pros inside a list"
    )
    cons: Optional[list[str]] = Field(
        default=None,
        description="Write down all the cons inside a list"
    )
    name: Optional[str] = Field(
        default=None,
        description="Write the name of the reviewer"
    )

# with_structured_output forces Gemini to return data that matches Review schema
structured_model = model.with_structured_output(Review)

# Raw text model extracts structured data automatically
result = structured_model.invoke("""I’ve been using the Sony WH-1000XM5 headphones for about a month now, and overall I’m very impressed. The noise cancellation is easily the best I’ve experienced — it completely blocks out traffic and office chatter. Sound quality is rich and balanced, with deep bass that doesn’t overpower the vocals.

Battery life is excellent; I get almost 30 hours on a single charge, and the quick charge feature is super convenient. The touch controls are intuitive, though sometimes they register accidental swipes when adjusting the headphones.

Comfort is mostly great, but after 3–4 hours my ears start to feel warm. The design looks premium, but the plastic body doesn’t feel as durable as I expected at this price point.

Industry-leading noise cancellation
Excellent sound quality
Long battery life
Fast charging

Ears get warm after long sessions
Build feels slightly fragile

Review by Arjun Mehta

""")
# result is NOT a normal dict it is a Pydantic object
# print(result)
print(result.summary)
print(result.sentiment)
print(result.pros)