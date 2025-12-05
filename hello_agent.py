import os
# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Import Agent class and run function from ADK
from google.adk.agents import Agent
from google.adk.run import run
# from google.adk.tools import Tool  # Uncomment if you want to use tools

MODEL = "gemini-2.5-flash"  # Model name for the agent
SYSTEM_INSTRUCTION = ("You are a helpful assistant. Keep answers short and crisp")  # System prompt

agent = Agent(
    name = "hello_agent",  # Agent name
    model=MODEL,            # Model to use
    instruction = SYSTEM_INSTRUCTION,  # System instructions
    # tools = [] # omitted for simplicity
)


# Entry point for running the agent
if __name__ == "__main__":
    user_input = "What is agent development kit?"  # Example user input
    result = run(agent=agent, user_input=user_input)  # Run the agent with input
    print(result)  # Print the agent's response
