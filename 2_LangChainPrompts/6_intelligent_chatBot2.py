from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

# Chat history with labeled messages
chat_history = [
    SystemMessage(content="You are an intelligent chatbot")
]

model = ChatGoogleGenerativeAI(model="gemini-flash-lite-latest")

print("I'm an AI chatbot!!! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=user_input))

    # Send full conversation history
    response = model.invoke(chat_history)

    # Add AI response to history
    chat_history.append(response)

    print("AI:", response.content)

print("\nFinal chat history:")
print(chat_history)


