from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

parser = JsonOutputParser()

format_instructions = parser.get_format_instructions()

prompt = PromptTemplate(
    template=
    """
    Analyze the customer review and return JSON
    Review: {review}
    {format_instructions}
    """,
    input_variables=["review"],
    partial_variables={"format_instructions": format_instructions}
)

# HuggingFace model
llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-4.7",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

review_text = """
The phone battery lasts forever and camera quality is amazing.
But the phone gets hot while gaming.
Overall I’m happy with the purchase.
"""

chain = prompt | model | parser

response = chain.invoke({"review": review_text})

print(response)


"""
NOTES:

    1. JsonOutputParser forces the LLM to return structured JSON.
    It also converts the response into a Python dictionary.

    2. parser.get_format_instructions() generates hidden rules
    that teach the model how to format output correctly.

    3. partial_variables automatically inject parser instructions
    into the prompt without the user providing them.

    4. PromptTemplate combines:
    - user input (review)
    - formatting rules (JSON schema)

    5. ChatHuggingFace wrapper converts HuggingFace endpoint
    into a chat-style model compatible with LangChain chains.

    6. Chain flow:
    Prompt → Model → Parser → Structured JSON

    7. Template variable names must match invoke keys exactly.

    8. Final output is machine-readable JSON,
    safe for APIs, databases, or automation.
"""

