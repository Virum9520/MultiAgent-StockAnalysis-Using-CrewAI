from crewai import Agent
from langchain_community.chat_models import ChatOpenAI
from config import OPENAI_API_KEY

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3, openai_api_key=OPENAI_API_KEY)

def create_team_lead():
    return Agent(
        role="Team Lead",
        goal="Aggregate insights into a structured investment report",
        backstory="You're a financial team lead preparing a final investor summary",
        llm=llm,
        verbose=True
    )