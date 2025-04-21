# agents/strategist.py

from crewai import Agent
from langchain_community.chat_models import ChatOpenAI
from config import OPENAI_API_KEY

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3, openai_api_key=OPENAI_API_KEY)

def create_stock_strategist():
    return Agent(
        role="Stock Strategist",
        goal="Recommend the top-performing and undervalued stocks",
        backstory="You provide practical stock investment strategies",
        llm=llm,
        verbose=True
    )
