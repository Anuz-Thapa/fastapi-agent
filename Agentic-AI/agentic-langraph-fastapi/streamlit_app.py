import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="AI Agentic Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Title and description
st.title("AI Agentic Chatbot")
st.markdown("Chat with multiple models with web search capabilities")

# Sidebar configuration
with st.sidebar:
    st.header("Agent Configuration")
    model_provider = st.selectbox("Model Provider", ['groq', 'openai'])
    model_name = st.selectbox("Model Name", ["llama3-70b", "gpt-4o-mini"])
    system_prompt = st.text_area(
        "System Prompt",
        value="Act as a personal smart AI assistant",
        height=100
    )
    allow_search = st.checkbox("Allow Web Search", value=False)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for role, msg in st.session_state.chat_history:
    if role == "user":
        with st.chat_message("user"):
            st.markdown(msg)
    else:
        with st.chat_message("assistant"):
            st.markdown(msg)

# Chat input
user_query = st.chat_input("Enter your query here")
if user_query:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.chat_history.append(("user", user_query))

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # For Streamlit Cloud, we'll use the deployed FastAPI endpoint
                # You'll need to replace this with your deployed API URL
                api_url = os.getenv("API_URL", "http://localhost:4000")
                
                payload = {
                    "model_name": model_name,
                    "model_provider": model_provider,
                    "system_prompt": system_prompt,
                    "message": [user_query],
                    "allow_search": allow_search
                }
                
                response = requests.post(f"{api_url}/chat", json=payload)
                response_data = response.json()
                
                st.markdown(response_data)
                st.session_state.chat_history.append(("assistant", response_data))
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Make sure your API is running and accessible.") 