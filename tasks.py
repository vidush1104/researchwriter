from crewai import Task
from tools import tool
from agents import news_researcher, news_writer

# Research Task — assigned to the Senior Researcher agent.
# The description tells the agent exactly what to investigate and what the
# final deliverable should look like. {topic} is injected at runtime via crew.kickoff().
research_task = Task(
    description=(
        "Identify the next big trend in {topic}."
        "Focus on identifying the pros and cons and overall narrative."
        "Your final report should clearly articulate the key points,"
        "its market opportunities, and potential risks"
    ),
    # Defines what a successful output looks like — CrewAI uses this to
    # evaluate whether the agent has completed the task properly.
    expected_output="A comprehensive 3 paragraph long report on the latest AI trends,",
    tools=[tool],          # Serper search tool so the researcher can pull live data
    agent=news_researcher, # This task is owned by and executed by the researcher
)

# Writer Task — assigned to the Writer agent.
# It runs after research_task completes and automatically receives the
# researcher's output as context, so the writer knows what was found.
writer_task = Task(
    description=(
        "Compose an insightful article on {topic}."
        "Focus on the latest trends and how it's impacting the industry."
        "This article must be very easy to understand, engaging and positive."
    ),
    # The expected output is markdown so it renders cleanly in the saved file.
    expected_output="A 3 paragraph article on {topic} advancements formatted as markdown.",
    tools=[tool],          # Writer can do additional searches if it needs more detail
    agent=news_writer,     # This task is owned by and executed by the writer
    async_execution=False, # Wait for this task to fully finish before moving on
    output_file='new-blog-post.md'  # Final article is saved here automatically
)