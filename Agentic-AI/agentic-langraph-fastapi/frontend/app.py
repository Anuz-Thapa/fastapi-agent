import streamlit as st 
import requests 

st.set_page_config(page_title="AI agentic chatbot",layout="centered")
st.title("AI Agent Chatbot")
st.markdown("Chat with multiple model with web search capabilities")

with st.sidebar:
    st.header("Agent Configuration")
    model_provider=st.selectbox("Model Provider",['groq','openai'])
    model_name=st.selectbox("Model Name",["llama3-70b-8192","gpt-4o-mini"])
    system_prompt=st.text_area(
        "System Prompt",
        value="Act as an personal smart ai assistant",
        height=100
    )
    allow_search=st.checkbox("Allow Web Search",value=False)

# session history for chat history

if "chat_history" not in st.session_state:
         st.session_state.chat_history=[]
for role,msg in st.session_state.chat_history:
    if role=="user":
        with st.chat_message("user"):
            st.markdown(msg)
    else:
        with st.chat_message("assistant"):
            st.markdown(msg)
user_query=st.chat_input("enter your query here")  #get user query
if user_query:
    with st.chat_message("user"):  #create a chat container for user query
        st.markdown(user_query)
    st.session_state.chat_history.append(("user",user_query))


# sending request to backend
    with st.chat_message("assistant"): #create a chat container for ai response
        with st.spinner("Thinking..."):
            try:
                api_url=os.getenv("API_URL","http://localhost:4000")
                payload={
                    "model_name":model_name,
                    "model_provider":model_provider,
                    "system_prompt":f"""{system_prompt}
                                    If web search is enabled, use it to find current information when:
                                    1. Asked about recent events or news
                                    2. Asked about current trends or developments
                                    3. Asked about topics that might need up-to-date information
                                    4. You're unsure about the current state of something
                                    Always verify information using the search tool when in doubt."""
                                ,
                    "message":[user_query],
                    "allow_search":allow_search
                }
                res=requests.post(f"{api_url}",json=payload)
                response=res.json()
                print(response)
                st.markdown(response)
                st.session_state.chat_history.append(("assistant",response))
            except Exception as e:
                st.error(f"Error: {e}")