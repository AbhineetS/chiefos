from memory.memory import global_memory

async def get_company_okrs() -> str:
    """Retrieve the current strategic goals and OKRs for the company."""
    print(f"\n[Tool Execution: Strategy Tracker] Fetching company OKRs...")
    
    # Mocked OKR retrieval
    result = (
        "Q3 Strategic OKRs:\n"
        "1. Increase AI product adoption by 25%\n"
        "2. Launch ChiefOS enterprise tier by September\n"
        "3. Reduce cloud infrastructure costs by 15%\n"
    )
    
    global_memory.set("current_okrs", result)
    return result
