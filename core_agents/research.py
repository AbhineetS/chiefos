from core_agents.engine import Agent, handoff
from tools.search import web_search

research_agent = Agent(
    name="Research Analyst",
    instructions="""You are the Research Analyst.
Your job is to gather information using the web_search tool.
Be extremely thorough and fetch all necessary information.
Once you have the information, summarize it and transfer back to the Executive Planner.
You must always use the transfer_to_executive_planner tool when finished.
""",
    tools=[web_search]
)
