"""
RunnablePassthrough Challenge
User gives a topic.
You must return:
{
  "topic": original input,
  "joke": generated joke
}
So the pipeline must:
👉 keep original topic
👉 generate joke
👉 return both
"""

from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="zai-org/GLM-4.7",
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)
parser = JsonOutputParser()
format_instructions = parser.get_format_instructions()

prompt = PromptTemplate(
    template="""Write a funny joke about this {topic}
    {format_instructions}""",
    input_variables=["topic"],
    partial_variables={"format_instructions" : format_instructions}
)

chain = prompt | model | parser

parallel_chain = RunnableParallel({
    "topic": RunnablePassthrough(),
    "joke": chain
})

response = parallel_chain.invoke({"topic": "Indian cricket team"})

print(response)


"""

# RunnablePassthrough
# Returns input unchanged
# Used to preserve original data
# Returns exactly what it receives
# Example: input {"topic": "AI"} → returns {"topic": "AI"}
# Mental model: identity wire

"""


"""
Issue Explanation:

RunnablePassthrough forwards the ENTIRE input dictionary unchanged.
Our input to the pipeline is:

    {"topic": "Indian cricket team"}

When RunnableParallel runs:

    "topic": RunnablePassthrough()

it returns the full dictionary again, not just the string value.
So the output becomes nested:

    {'topic': {'topic': 'Indian cricket team'}}

This happens because RunnableParallel wraps each branch result
under its key name. Since passthrough already returned a dict,
we ended up with a dict inside a dict.

Fix:

We must extract only the string value of "topic".
We use RunnableLambda to reshape the data:

    RunnablePassthrough() | RunnableLambda(lambda x: x["topic"])

RunnableLambda acts like a small transformer that converts:

    {"topic": "..."}  →  "..."

Now the final output correctly becomes:

{
  "topic": "Indian cricket team",
  "joke": "generated joke"
}

Key concept:

RunnablePassthrough = preserve input
RunnableLambda = reshape/clean input
RunnableParallel = merge multiple branches

Together they let us preserve raw data AND generate AI output
without unwanted nesting.
"""
