from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver
import datetime
import urllib.request
import urllib.parse

@tool
def get_current_time() -> str:
    """Returns the current date and time. Use this when the user asks about today, tomorrow, or current events."""""
    return datetime.datetime.now().strftime("%A, %B %d, %Y %I:%M %p")

@tool
def get_weather(city: str) -> str:
    """Fetches the live current weather for a given city. Always use this when a user asks for the weather."""
    try:
        safe_city = urllib.parse.quote(city)
        url = f"https://wttr.in/{safe_city}?format=3"
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8').strip()
    except Exception as e:
        return f"Could not fetch weather for {city}. Error: {e}"

    

load_dotenv()

def main():
    model = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0)
    tools = [get_current_time, get_weather]

    memory = MemorySaver()

    agent_executor = create_agent(model, tools, checkpointer=memory)
    config = {"configurable": {"thread_id": "my_first_chat"}}

    print("Welcome! I am your AI assistant. Type 'quit' to exit.")
    print("You can ask me anything.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            print("Goodbye!")
            break

        print("\nAssistant: ", end="", flush=True)

        response = agent_executor.invoke(
            {"messages": [HumanMessage(content=user_input)]},
            config=config
        )
        ai_message = response["messages"][-1].content

        if isinstance(ai_message, list) and len(ai_message) > 0:
            print(ai_message[0].get("text", ""))
        else:
            print(ai_message)

if __name__ == "__main__":
    main()