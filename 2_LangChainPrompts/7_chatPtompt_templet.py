"""
Chat templet is used for multi turn chat at run time

Message place holder is used here os {domain} & {topic}
    In langChain it is a spacial place holder used inside a chat-prompt-template
    to dinamically insert chat history of list of messages at runtime.

    Use Case :
        ChatBot to customer
        - User : I want refund for order #122
        - chat bot : your refund has been initated for #122

        -> after few days.

        - customer: ask where is my refund. 
        - Chatbot must have the old chat history to reply to the customer,

        there Message placeholder is used
"""

from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket',
                               'topic':'Dusra'})

print(prompt)