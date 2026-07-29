from agents import Agent
from tools.calendar import get_upcoming_meetings

meeting_prep_agent = Agent(
    name="Meeting Preparation Agent",
    instructions=(
        "You are responsible for reviewing the calendar and preparing meeting briefings. "
        "Use the calendar tool to find out about upcoming meetings and provide a quick agenda/briefing based on the date provided."
    ),
    tools=[get_upcoming_meetings],
)
