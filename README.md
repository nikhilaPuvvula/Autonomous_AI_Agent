# **🤖 Autonomous AI Agent**

An intelligent, modular AI system built using LangChain, LangGraph, and OpenAI that can:
1) Fetch real-time weather,
2) Convert currencies,
3) Perform calculations,
4) Execute small Python code snippets, and
5) Search the web — all through a simple Streamlit UI.

**Tech Stack**

1) Python 3.10+
2) LangChain 1.x
3) OpenAI GPT-4o-mini
4) Streamlit
5) DuckDuckGo Search API
6) Requests / Open-Meteo / ExchangeRate APIs

**Features**

1) Multi-Tool Agent: ReAct-based agent capable of reasoning and choosing tools dynamically.
2) Weather Lookup: Fetches real-time weather data for any city using the Open-Meteo API.
3) Currency Converter: Converts between any two world currencies using ExchangeRate API.
4) Web Search: Uses DuckDuckGo for quick factual lookups.
5) Python Code Runner: Executes small, safe code snippets and returns variable results.
6) User-Friendly UI: Built with Streamlit for interactive chat-like experience.

**Project Structure**

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

**Streamlit Results**

<img width="1887" height="848" alt="autonomous_ai_1" src="https://github.com/user-attachments/assets/1e179ac3-9327-423e-94b9-aa4b80b5aa76" />

<img width="1912" height="855" alt="autonomous_ai_2" src="https://github.com/user-attachments/assets/33b4efa7-e26f-43db-b2ff-398e1da80f3a" />


