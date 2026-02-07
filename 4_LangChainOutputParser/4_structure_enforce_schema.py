
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)


"""
### StructuredOutputParser Notes

StructuredOutputParser forces the LLM to return output in a fixed JSON structure.
It enforces keys but does NOT validate data types.

Flow:
Schema → format instructions → model → structured JSON → Python dict

Key components:

1. ResponseSchema
   Defines expected JSON fields

2. StructuredOutputParser
   Builds JSON rules from schema

3. get_format_instructions()
   Injects hidden formatting rules into prompt

4. PromptTemplate + partial_variables
   Adds JSON instructions automatically

5. Chain
   prompt → model → parser

Use cases:
- predictable JSON output
- extraction tasks
- lightweight structure enforcement

Difference from Pydantic:
Structured parser enforces shape
Pydantic parser enforces shape + validation
"""