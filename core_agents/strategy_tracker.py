from core_agents.engine import Agent
from tools.strategy import get_company_okrs

strategy_tracker_agent = Agent(
    name="Strategy Tracker",
    instructions="""You are the Strategy Tracker.
Your job is to monitor strategic goals and provide updates on company OKRs.
Always use your get_company_okrs tool when asked about strategy or OKRs.
Once you have the information, transfer control back to the Executive Planner.
""",
    tools=[get_company_okrs]
)
