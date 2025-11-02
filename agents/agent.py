# agents/agent.py  –  works with LangChain 1.x

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from agents.tools import (
    get_weather_data,
    convert_currency,
    calculate,
    run_python_code,
    web_search,
)

# Load environment variables
load_dotenv()

# Step 1: Initialize the LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Step 2: Wrap your functions as tools
tools = [
    get_weather_data,
    convert_currency,
    calculate,
    run_python_code,
    web_search,
]

# Step 3: Create the ReAct-style agent using LangGraph
agent_executor = create_react_agent(
    model=llm,
    tools=tools,
    debug=True,
)

# Optional quick test
if __name__ == "__main__":
    result = agent_executor.invoke({"messages": [("user", "What is the weather in Bhubaneswar?")]})
    print(result["messages"][-1].content)
