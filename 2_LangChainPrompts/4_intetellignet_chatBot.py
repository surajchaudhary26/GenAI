from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# let's store it's chat history

chat_history = []


model = ChatGoogleGenerativeAI(model='gemini-flash-lite-latest')
print("i'm anhi Ai chatbot!!!!")
while True:
    user_input = input('You: ')
    chat_history.append(user_input)

    if user_input == 'exit':
        break

    response = model.invoke(chat_history)
    chat_history.append(response.content)
    print('Ai : ', response.content)
    

print(chat_history)

"""
This is a bit intelligetn bot
somehow it is maintaing chat history and based on that it is answring next question

For better understanding go through... chats
----------------------------------------------------------------------------------------------------------------------------

(.venv) surajchaudhary@surajs-MacBook-Air-6 ~/SurajSpace/Learning/GenAi/2_LangChainPrompts python3 4_intetellignet_chatBot.py 
i'm anhi Ai chatbot!!!!
You: guess two numbers between 1 to 10.
Ai :  I'll guess **4** and **9**.
You: now from your guessed numbers multipy greater number by 2
Ai :  The two numbers I guessed are **4** and **9**.

The greater number is **9**.

Multiplying the greater number by 2: $9 \times 2 = 18$.
You: exit


['guess two numbers between 1 to 10.', "I'll guess **4** and **9**.", 
'now from your guessed numbers multipy greater number by 2',
 'The two numbers I guessed are **4** and **9**.
 \n\nThe greater number is **9**.\n\nMultiplying the greater number by 2: $9 \\times 2 = 18$.',
   'exit']
----------------------------------------------------------------------------------------------------------------------------

But still it has some problem...

- Since the chat history is very tiny... That's why it is able to fetch the data
- But when chat history will be larger it will fail to indentify relivant part of chat_history in order to give desireble output
- Because it has no level with is means which msg is from user and which msg form AI

- this problem is solved by LangChain.. by types of Message
    1. System message.
    2. AI message.
    3. Human message.

"""