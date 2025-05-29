# AI Agentic Chatbot

A chatbot application that uses multiple AI models with web search capabilities.

## Deployment Instructions

### 1. Deploy the FastAPI Backend
1. Choose a hosting platform (e.g., Heroku, DigitalOcean, AWS)
2. Deploy your FastAPI application
3. Note down the deployed API URL

### 2. Deploy on Streamlit Cloud
1. Push your code to a GitHub repository
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app and connect your GitHub repository
4. Set the main file path to `streamlit_app.py`
5. Add the following secrets in Streamlit Cloud:
   - `GROQ_API_KEY`: Your Groq API key
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `TAVILY_API_KEY`: Your Tavily API key
   - `API_URL`: Your deployed FastAPI backend URL

## Environment Variables
Create a `.env` file with the following variables:
```
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
API_URL=your_deployed_api_url
```

## Local Development
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the FastAPI backend:
```bash
python main.py
```

3. Start the Streamlit frontend:
```bash
streamlit run streamlit_app.py
```

## Features
- Multiple AI model support (Groq, OpenAI)
- Web search capabilities using Tavily
- Configurable system prompts
- Chat history
- Modern UI with Streamlit

