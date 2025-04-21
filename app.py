import streamlit as st
import plotly.graph_objects as go
import yfinance as yf
from config import OPENAI_API_KEY
from utils.finance import compare_stocks, get_company_info, get_company_news
from agents.analyst import create_market_analyst
from agents.researcher import create_company_researcher
from agents.strategist import create_stock_strategist
from agents.lead import create_team_lead
from crewai import Task, Crew

st.set_page_config(page_title="AI Investment Strategist", layout="wide")

st.markdown("""
    <h1 style="text-align: center; color: #4CAF50;">📈 AI Investment Strategist</h1>
    <h3 style="text-align: center; color: #6c757d;">Generate personalized investment reports with the latest market insights.</h3>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
    <h2 style="color: #343a40;">Configuration</h2>
    <p style="color: #6c757d;">Enter stock symbols for detailed insights and recommendations.</p>
""", unsafe_allow_html=True)

input_symbols = st.sidebar.text_input("Enter Stock Symbols (comma-separated)", "AAPL, TSLA, GOOG")
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
stocks_symbols = [s.strip() for s in input_symbols.split(",") if s.strip()]

if st.sidebar.button("Generate Investment Report"):
    if not api_key:
        st.sidebar.warning("Please enter your OpenAI API Key.")
    else:
        OPENAI_API_KEY = api_key

        market_analyst = create_market_analyst()
        company_researcher = create_company_researcher()
        stock_strategist = create_stock_strategist()
        team_lead = create_team_lead()

        # Tasks
        task1 = Task(
            description=f"Analyze stock performance for: {stocks_symbols}",
            expected_output="Percentage performance change per stock",
            agent=market_analyst
        )

        task2 = Task(
            description=f"Research company profiles and news: {stocks_symbols}",
            expected_output="Company overviews and latest news headlines",
            agent=company_researcher
        )

        task3 = Task(
            description="Provide top stock recommendations based on analysis",
            expected_output="Top 3 investment picks",
            agent=stock_strategist
        )

        task4 = Task(
            description="Compile a final investor report with ranked suggestions",
            expected_output="Final investment report for user",
            agent=team_lead
        )

        crew = Crew(
            agents=[market_analyst, company_researcher, stock_strategist, team_lead],
            tasks=[task1, task2, task3, task4],
            verbose=True
        )

        report = crew.kickoff()

        st.subheader("Investment Report")
        st.markdown(report)

        st.markdown("### 📊 Stock Performance (6-Months)")
        stock_data = yf.download(stocks_symbols, period="6mo")["Close"]

        fig = go.Figure()
        for symbol in stocks_symbols:
            fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data[symbol], mode='lines', name=symbol))

        fig.update_layout(title="Stock Performance Over Last 6 Months", xaxis_title="Date", yaxis_title="Price (USD)", template="plotly_dark")
        st.plotly_chart(fig)