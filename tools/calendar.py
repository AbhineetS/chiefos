from agents.decorators import tool
from memory.memory import global_memory
from datetime import datetime

@tool
async def get_upcoming_meetings(date_str: str) -> str:
    """Retrieve upcoming meetings from the calendar for a given date (YYYY-MM-DD)."""
    print(f"\n[Tool Execution: Calendar] Checking events for: {date_str}")
    
    # Mocked calendar retrieval
    result = (
        f"Meetings on {date_str}:\n"
        f"1. 10:00 AM - Team Sync\n"
        f"2. 02:00 PM - Client Review Session\n"
        f"3. 04:30 PM - Planning Meeting"
    )
    
    global_memory.set(f"meetings_{date_str}", result)
    return result
