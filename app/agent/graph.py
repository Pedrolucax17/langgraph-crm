import os
from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from app.agent.tools import add_client, find_client
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model("openai:gpt-4o-mini", temperature=0)
agent = create_react_agent(
    model,
    tools=[add_client, find_client]
)