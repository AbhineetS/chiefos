from memory.memory import global_memory
import asyncio

async def draft_and_send_email(to_email: str, subject: str, body: str) -> str:
    """Drafts an email and asks for human approval before sending."""
    print(f"\n[Tool Execution: Gmail] Drafting email to: {to_email}")
    print(f"Subject: {subject}")
    print(f"Body:\n{body}\n")
    
    # Prompt the human in the terminal
    approval = input(">>> Approve this email for sending? (y/n): ")
    if approval.strip().lower() != 'y':
        return "Email sending cancelled by user."
    
    global_memory.set("last_email_sent", {"to": to_email, "subject": subject})
    return f"Email successfully drafted and sent to {to_email}."
