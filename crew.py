from crewai import Crew, Process
from tasks import research_task, writer_task
from agents import news_writer, news_researcher

# Assemble the crew with both agents and their assigned tasks.
# The order of agents and tasks matters — they run in the sequence listed below.
crew = Crew(
    agents=[news_researcher, news_writer],   # Researcher goes first, writer second
    tasks=[research_task, writer_task],      # Tasks are paired to agents in tasks.py
    process=Process.sequential,              # Run tasks one after another, not in parallel
    verbose=True                             # Show live execution logs in the terminal
)

# Kick off the crew with a specific topic injected at runtime.
# The {topic} placeholder in every agent goal, backstory, and task description
# gets replaced with this value before execution starts.
result = crew.kickoff(inputs={'topic': 'Which is better - Working in US or India?'})

# Print the final output — this will be the writer's finished article.
# It's also saved to new-blog-post.md as configured in writer_task.
print(result)