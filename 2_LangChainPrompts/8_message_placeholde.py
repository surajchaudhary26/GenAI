"""
Docstring for 2_LangChainPrompts.8_message_placeholde

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


from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []
# load chat history
with open('2_LangChainPrompts/chat_history.txt') as f:
    chat_history.extend(f.readlines()) # appending in chat_history list

print(chat_history)

# create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(prompt)