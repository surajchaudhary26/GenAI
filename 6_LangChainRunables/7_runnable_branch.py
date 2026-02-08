"""
RunnableBranch Challenge Goal

If the generated joke is too long → summarize it
Else → return joke as is

You are building:

joke → decision → (summarize OR keep)

Expected behavior

Short joke → unchanged
Long joke → summarized

Final output is always text.

Requirements:
 - generate joke first
 - check word count
 - use RunnableBranch
 - only summarize if joke > 20 words

"""
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnablePassthrough, RunnableLambda
from dotenv import load_dotenv
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-4.7",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()

# 1. Joke generator
joke_prompt = PromptTemplate.from_template(
    "Tell a long funny joke about {topic}"
)
joke_chain = joke_prompt | model | parser

"""
# 2. Summary chain
RunnableLambda wraps the joke string into a dictionary 
so the summary prompt receives the variable it expects.
"""

summary_prompt = PromptTemplate.from_template(
    "Summarize this joke in one sentence:\n{joke}"
)
# summary_prompt expects dict joke
summary_chain = RunnableLambda(lambda joke: {"joke": joke}) | summary_prompt | model | parser 

"""
3. Condition function 
 - return ture if len(joke) > 20
 - return false if len(joke) < 20 """
def is_long(text):
    return len(text.split()) > 20 


"""
# 4. Branch logic

RunnableBranch reads:
( condition , what to run if True )
else → default branch

So:
(is_long, summary_chain)

means:
if is_long(text) is True → run summary_chain
and
RunnablePassthrough()

"""
branch = RunnableBranch(
    (is_long, summary_chain),
    RunnablePassthrough()
)

"""
# 5. Full pipeline
           ┌──────── summarize
joke ── decision
           └──────── keep original
"""
pipeline = joke_chain | branch

result = pipeline.invoke({"topic": "AI engineers"})

print(result)

"""
# RunnableBranch
# Conditional execution (if/else)
# Returns output of selected branch
# Only one branch runs
# Used for decision logic
# Mental model: decision tree node

"""