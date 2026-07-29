from agents.decorators import tool
from memory.memory import global_memory

@tool
async def web_search(query: str) -> str:
    """Search the web for information. Use this whenever you need up-to-date facts or research."""
    print(f"\n[Tool Execution: Web Search] Searching for: '{query}'")
    
    # Mocking actual search logic for the MVP
    result = f"Search Results for '{query}': Found comprehensive details regarding '{query}'. The information is current and accurate."
    
    # Store the result in shared memory for other agents to potentially reference
    global_memory.set(f"search_{query}", result)
    
    return result
