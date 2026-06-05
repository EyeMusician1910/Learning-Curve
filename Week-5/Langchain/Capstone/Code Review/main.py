import streamlit as st
import langchain_helper as lch
from langchain_community.chat_message_histories import SQLChatMessageHistory
from pathlib import Path
import os

st.set_page_config(layout="wide")
st.title("Code Assitant")

# ─── PERMANENT SQLITE DATABASE LAYER ────────────────────────────────
DB_FILE = "sqlite:///chat_history.db"
SESSION_ID = "local_developer_session"

if "chat_memory" not in st.session_state:
    st.session_state.chat_memory = SQLChatMessageHistory(
        session_id=SESSION_ID,
        connection=DB_FILE
    )

@st.cache_resource
def load_agent():
    return lch.get_agent_executor()

agent_executor = load_agent()

# Display Chat History logs directly out of the local SQLite rows
st.subheader("💬 Active Agent Session")
for msg in st.session_state.chat_memory.messages:
    role = "User" if msg.type == "human" else "Assistant"
    st.markdown(f"**{role}:** {msg.content}")
st.write("---")

# Quick flush tool for developer convenience
if st.sidebar.button("🗑️ Clear Permanent Chat Logs"):
    st.session_state.chat_memory.clear()
    st.success("Database table rows flushed clean!")
    st.rerun()

# Multi-line text layout input with native Ctrl+Enter mapping functionality
user_query = st.text_area(
    "Ask your Agent to inspect books or write/execute a script:", 
    placeholder="e.g., Write a python function to compute factorials and execute it with input 5 to verify logs...", 
    height=120
)

if user_query:
    st.markdown(f"**User:** {user_query}")
    
    with st.spinner("Agent is invoking model chains and analyzing tools..."):
        try:
            # Execute modern invocation payload dictionaries
            response = agent_executor.invoke({
                "input": user_query,
                "chat_history": st.session_state.chat_memory.messages
            })
            
            final_output = response["output"]
            st.markdown(f"**Assistant:** {final_output}")
            
            # Save conversations securely to local SQLite tables
            st.session_state.chat_memory.add_user_message(user_query)
            st.session_state.chat_memory.add_ai_message(final_output)
            
        except Exception as e:
            st.error(f"Agent Framework Error: {e}")