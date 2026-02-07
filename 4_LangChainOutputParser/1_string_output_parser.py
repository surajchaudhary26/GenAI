from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
# model
model = ChatGoogleGenerativeAI(model="gemini-flash-lite-latest")

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'black hole'})
result = model.invoke(prompt1)
prompt2 = template2.invoke({'text':result.content})
result1 = model.invoke(prompt2)


print(result.content)
print(result1.content)

"""
It has some issue

Notes:

1. model.invoke() does NOT return a string.
   It returns an AIMessage object.

2. AIMessage contains:
   - content (actual text)
   - metadata (tokens, model info, etc.)

3. To reuse LLM output, we must extract:
   result.content

4. We manually pass output of one prompt into another:
   report → summary

5. This works but is inefficient because:
   - model is called twice manually
   - code becomes long
   - chaining is cleaner

6. LangChain chains solve this by:
   prompt1 | model | prompt2 | model
   automatically passing outputs.

"""