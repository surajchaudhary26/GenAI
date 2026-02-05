from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-flash-lite-latest')
print("i'm anhi Ai chatbot!!!!")
while True:
    user_input = input('You: ')
    if user_input == 'exit':
        break
    response = model.invoke(user_input)
    print('Ai : ', response.content)
    

"""
This chatBot has a problem!!!
It dosen't remeber that past history

Read this chat for better understanding...
------------------------------------------------------------------------------------------------------
i'm anhi Ai chatbot!!!!
You: guess two numbers
Ai :  That's a fun challenge! Since you haven't given me any clues, I'll pick two random numbers.

How about **7** and **42**?

Are those close to what you were thinking? Tell me if you'd like me to try guessing again with a hint!
You: which is smaller
Ai :  Please provide me with the two things you would like me to compare!

I need to know **what** you want me to determine is smaller. For example, are you comparing:

* **Numbers?** (e.g., 5 or 10)
* **Fractions?** (e.g., 1/2 or 1/4)
* **Measurements?** (e.g., 1 meter or 1 centimeter)
* **Words or concepts?** (This is trickier, but I'll try my best!)

------------------------------------------------------------------------------------------------------
"""