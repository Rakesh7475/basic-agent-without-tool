import os
from dotenv import load_dotenv
load_dotenv()
from google.adk.agents import Agent
from google.adk.run import run
# from google.adk.tools import Tool

MODEL = "gemini-2.5-flash"
SYSTEM_INSTRUCTION = ("You are a helpful assistant.Keep answers short and crisp")

agent = Agent(
    name = "hello_agent",
    model=MODEL,
    instruction = SYSTEM_INSTRUCTION,
    # tools = [] # ommitted for simplicity
)

if __name__ == "__main__":
    user_input = "What is agent development kit?"
    result = run(agent=agent, user_input=user_input)
    print(result)
