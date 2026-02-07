from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='zai-org/GLM-4.7',
    task='text-generation'
)
model = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

# Step 1 → classify sentiment
sentiment_classifier = PromptTemplate(
    template="Classify the sentiment of this feedback as positive or negative:\n{text}",
    input_variables=["text"]
)
classifier_chain = sentiment_classifier | model | parser

# Step 2A → positive response
positive_prompt = PromptTemplate(
    template="Write a friendly thank-you response to this feedback:\n{text}",
    input_variables=["text"]
)
positive_chain = positive_prompt | model | parser

# Step 2B → negative response
negative_prompt = PromptTemplate(
    template="Write an apology and support response:\n{text}",
    input_variables=["text"]
)
negative_chain = negative_prompt | model | parser

# Conditional router

router = RunnableBranch(
    (lambda text: "positive" in classifier_chain.invoke(text).lower(), positive_chain),
    negative_chain
)

feedback = "The product works great and I love the design!"
response = router.invoke({"text": feedback})

print(response)


"""
feedback
  ↓
classifier_chain
  ↓
RunnableBranch -> lambda condition
  ↓
True? → positive_chain
False? → negative_chain



lambda is a small decision function.
RunnableBranch uses lambda to choose which chain runs.
It works like if/else for LLM pipelines.
Lambda returns True/False → branch executes.

"""