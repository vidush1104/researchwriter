from crewai import Agent, LLM
from langchain_openai import ChatOpenAI
import os
from tools import tool
from dotenv import load_dotenv

# Load environment variables from .env file (GOOGLE_API_KEY, SERPER_API_KEY, etc.)
load_dotenv()

# Note: memory=False on agents below because CrewAI's built-in memory defaults
# to OpenAI's gpt-4o-mini. Since we're not using OpenAI, we disable it to avoid errors.
llm = LLM(
    model="gemini/gemini-2.5-flash",
    temperature=0.5,       # Balanced between creativity and factual accuracy
    api_key=os.getenv("GOOGLE_API_KEY")
)

# The researcher is responsible for gathering information on the given topic.
# It's allowed to delegate subtasks to other agents if needed (allow_delegation=True).
# We give it the Serper web search tool so it can look up real-time information.
news_researcher = Agent(
    role="Senior Researcher",
    goal='Uncover ground breaking technologies in {topic}',
    verbose=True,          # Print step-by-step reasoning to the console
    memory=False,          # Disabled — would require an OpenAI key to function
    backstory=(
        "Driven by curiosity, you're at the forefront of innovation, "
        "eager to explore and share knowledge that could change the world."
    ),
    tools=[tool],          # Serper search tool for live web lookups
    llm=llm,
    allow_delegation=True  # Can hand off work to other agents in the crew
)

# The writer takes the researcher's findings and turns them into a readable article.
# It does not delegate — its sole job is to write clear, engaging content.
news_writer = Agent(
    role="Writer",
    goal='Write engaging articles about {topic}',
    verbose=True,          # Print step-by-step reasoning to the console
    memory=False,          # Disabled — would require an OpenAI key to function
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    tools=[tool],          # Can search for extra details if needed while writing
    llm=llm,
    allow_delegation=False # Writer stays focused — no delegating to other agents
)