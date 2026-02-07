from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-flash-lite-latest")

class PersonSchema(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=PersonSchema)
format_instruction = parser.get_format_instructions()

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':format_instruction}
)

chain = template | model | parser

final_result = chain.invoke({'place':'India'})

print(final_result)

"""
PydanticOutputParser enforces schema validation on LLM output.
It injects format instructions into the prompt automatically.
The parser validates types and constraints using Pydantic.
The final output is a real Python object, not text.
This is production-safe structured extraction.
"""