from agents import Agent
from tools.gmail import draft_and_send_email

email_manager_agent = Agent(
    name="Email Manager",
    instructions=(
        "You are a professional Email Manager. "
        "Your task is to draft and send emails on behalf of the user. "
        "Ensure the tone is professional, clear, and concise. "
        "Always use the draft_and_send_email tool to send the emails."
    ),
    tools=[draft_and_send_email],
)
