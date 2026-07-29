from core_agents.engine import Agent, handoff
from tools.calendar import get_upcoming_meetings
from tools.pdf import extract_text_from_pdf

meeting_prep_agent = Agent(
    name="Meeting Preparation",
    instructions="""You are the Meeting Preparation Agent.
Your job is to check the calendar using the get_upcoming_meetings tool,
and read any necessary briefing PDFs using the extract_text_from_pdf tool.
Summarize the preparation material for the upcoming meetings and transfer back to the Executive Planner.
You must always use the transfer_to_executive_planner tool when finished.
""",
    tools=[get_upcoming_meetings, extract_text_from_pdf]
)
