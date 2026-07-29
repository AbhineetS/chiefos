from core_agents.engine import Agent, handoff
from tools.gmail import draft_and_send_email

# We need the planner agent to be able to be handed back to.
# Let's import planner_agent in the main or handle it correctly.
# But for now, email_manager just sends the email.

email_manager_agent = Agent(
    name="Email Manager",
    instructions="""You are the Email Manager.
Your job is to draft and send emails using the draft_and_send_email tool.
After sending the email, summarize the action taken and transfer back to the Executive Planner.
You must always use the transfer_to_executive_planner tool when finished.
""",
    tools=[draft_and_send_email]
)
