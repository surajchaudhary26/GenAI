from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-flash-lite-latest")

# Output json schema format
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}


structured_model = model.with_structured_output(json_schema)

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

# print(result)
print(result["sentiment"])
