# agents/researcher.py

from crewai import Agent
from langchain_community.chat_models import ChatOpenAI
from config import OPENAI_API_KEY

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3, openai_api_key=OPENAI_API_KEY)

def create_company_researcher():
    return Agent(
        role="Company Researcher",
        goal="Provide company overview and latest financial news",
        backstory="You're an equity researcher providing insights for investors",
        llm=llm,
        verbose=True
    )
