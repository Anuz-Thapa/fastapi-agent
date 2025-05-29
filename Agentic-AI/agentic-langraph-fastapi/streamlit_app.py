import streamlit as st
from agents.ai_agents import get_ai_response

st.title("AI Chat Interface")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        response = get_ai_response(prompt)
        st.markdown(response)
        
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response}) 