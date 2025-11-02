🤖 Autonomous AI Agent

An intelligent, modular AI system built using LangChain, LangGraph, and OpenAI that can:
1) Fetch real-time weather,
2) Convert currencies,
3) Perform calculations,
4) Execute small Python code snippets, and
5) Search the web — all through a simple Streamlit UI.

Features

1) Multi-Tool Agent: ReAct-based agent capable of reasoning and choosing tools dynamically.
2) Weather Lookup: Fetches real-time weather data for any city using the Open-Meteo API.
3) Currency Converter: Converts between any two world currencies using ExchangeRate API.
4) Web Search: Uses DuckDuckGo for quick factual lookups.
5) Python Code Runner: Executes small, safe code snippets and returns variable results.
6) User-Friendly UI: Built with Streamlit for interactive chat-like experience.

Project Structure

```
Autonomous_AI_Agents/
│
├── agents/
│   ├── tools.py          
│   ├── agent.py        
│
├── UI/
│   ├── app.py          
│
├── .env                  
├── requirements.txt      
└── README.md
```          
