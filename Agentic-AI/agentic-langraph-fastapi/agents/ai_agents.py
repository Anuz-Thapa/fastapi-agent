from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from agents.llm_provider import get_llm
from agents.tools import get_tools


def get_ai_response(llm_id,query,allow_search,system_prompt,provider):
    llm=get_llm(provider,llm_id)
    tools=get_tools(allow_search)

    # Enhance system prompt to use search when available
    enhanced_prompt = f"""{system_prompt}
    If web search is enabled, use it to find current information when:
    1. Asked about recent events or news
    2. Asked about current trends or developments
    3. Asked about topics that might need up-to-date information
    4. You're unsure about the current state of something
    Always verify information using the search tool when in doubt."""

    agent=create_react_agent(
        model=llm,
        tools=tools
    )
    # to built conversation history
    messages = [
        {"role": "system", "content": enhanced_prompt},
        {"role": "user", "content": query[-1]}
    ]
    
    state = {
        "messages": messages
    }

    response = agent.invoke(state)
    # Extract the AI's response content from the last message
    if response and "messages" in response:
        for message in reversed(response["messages"]):
            if isinstance(message, AIMessage):
                return message.content
    return "Sorry, I couldn't generate a response."

