# agents/analyst.py

from crewai import Agent
from langchain_community.chat_models import ChatOpenAI
from config import OPENAI_API_KEY

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3, openai_api_key=OPENAI_API_KEY)

def create_market_analyst():
    return Agent(
        role="Market Analyst",
        goal="Analyze and compare stock performance over 6 months",
        backstory="You are a stock market expert focusing on performance trends",
        llm=llm,
        verbose=True
    )
