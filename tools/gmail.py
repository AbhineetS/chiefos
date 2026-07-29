from agents.decorators import tool
from memory.memory import global_memory

async def _always_require_approval(_ctx, params, _call_id) -> bool:
    """Require human approval for sending any email."""
    return True

@tool(needs_approval=_always_require_approval)
async def draft_and_send_email(to_email: str, subject: str, body: str) -> str:
    """Draft and send an email to a recipient. 
    This action requires human approval before it is actually sent.
    """
    print(f"\n[Tool Execution: Gmail] Sending email...")
    print(f"To: {to_email}")
    print(f"Subject: {subject}")
    print(f"Body:\n{body}\n")
    
    global_memory.set("last_email_sent", {"to": to_email, "subject": subject})
    return f"Email successfully drafted and sent to {to_email}."
