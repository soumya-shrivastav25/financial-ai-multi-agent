import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

# Load environment variables from .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing from your .env file (no quotes)")

# Define LLM with Groq provider
groq_llm = LLM(
    model="groq/llama3-8b-8192",  # ✅ must have groq/ prefix
    api_key=GROQ_API_KEY
)

# Agents
financial_researcher = Agent(
    role="Financial Researcher",
    goal="Research and summarize the latest financial market trends.",
    backstory="An expert in analyzing stock markets, company earnings, and economic indicators.",
    verbose=True,
    allow_delegation=False,
    llm=groq_llm
)

financial_analyst = Agent(
    role="Financial Analyst",
    goal="Analyze research data and give investment recommendations.",
    backstory="Specialist in making investment decisions from research insights.",
    verbose=True,
    allow_delegation=False,
    llm=groq_llm
)

# Tasks — expected_output is required
task1 = Task(
    description="Gather the latest news and stock trends for the technology sector.",
    expected_output="A concise summary of the current technology sector market trends and major news events.",
    agent=financial_researcher
)

task2 = Task(
    description="Based on the research, recommend 3 technology stocks to watch or invest in.",
    expected_output="A list of 3 technology stocks with short reasoning for each recommendation.",
    agent=financial_analyst
)

# Crew
crew = Crew(
    agents=[financial_researcher, financial_analyst],
    tasks=[task1, task2],
    verbose=True
)

if __name__ == "__main__":
    result = crew.kickoff()
    print("\nFinal Output:\n", result)
