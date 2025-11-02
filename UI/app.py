# UI/app.py
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.agent import agent_executor
import streamlit as st

st.set_page_config(page_title="Autonomous AI Agent", page_icon="🤖")

st.title("🤖 Autonomous AI Agent")
st.write("Ask me anything! I can search, check weather, convert currencies, calculate, or run Python code.")

query = st.text_input("Enter your query:")

if st.button("Run Agent"):
    if query:
        with st.spinner("Thinking..."):
            result = agent_executor.invoke({"messages": [("user", query)]})
        st.success("✅ Done!")
        st.write(result["messages"][-1].content)
    else:
        st.warning("Please enter a query first.")
