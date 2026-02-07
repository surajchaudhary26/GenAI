from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()
# model
model = ChatGoogleGenerativeAI(model="gemini-flash-lite-latest")


parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()} # This generates hidden instructions like: JSON
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)



"""
### Notes — PromptTemplate + JsonOutputParser

This pipeline forces the LLM to return structured JSON instead of free text.

Flow:

User input → PromptTemplate → Model → JsonOutputParser → Python dict

Key concepts:

1. JsonOutputParser
   - Forces model to return JSON format
   - Converts output into a Python dictionary
   - Prevents messy text responses

2. parser.get_format_instructions()
   - Automatically generates JSON formatting rules
   - Injected into the prompt
   
3. partial_variables
   - Variables automatically added to template
   - User does NOT need to provide them
   - Used to inject parser instructions

4. PromptTemplate
   - Combines user topic + hidden JSON instructions
   - Ensures consistent structured output

5. Chain
   template → model → parser
   Automatically passes data through pipeline

Result:
The model returns clean JSON that is safe for APIs, databases, or automation.

Key takeaway:
Never trust raw LLM text. Use parsers to enforce structure.
"""