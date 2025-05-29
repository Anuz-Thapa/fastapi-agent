from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from app.config import GROQ_API_KEY,OPENAI_API_KEY

def get_llm(provider,model):
    if provider == "groq":
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is not set in the environment variables")
        return ChatGroq(model=model,api_key=GROQ_API_KEY)
    elif provider == "openai":
        if not OPENAI_API_KEY:
            raise ValueError("openai api key is not set in environment variables")
        return ChatOpenAI(model=model,api_key=OPENAI_API_KEY)
    else:
        raise ValueError(f"unknown provider:{provider}")


