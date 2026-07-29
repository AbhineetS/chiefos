from memory.memory import global_memory

async def web_search(query: str) -> str:
    """Search the web for information. Use this whenever you need up-to-date facts or research."""
    print(f"\n[Tool Execution: Web Search] Searching for: '{query}'")
    
    try:
        from duckduckgo_search import DDGS
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))
            
        if not results:
            result = f"No results found for '{query}'."
        else:
            result_str = f"Search Results for '{query}':\n"
            for r in results:
                result_str += f"- {r['title']}: {r['body']} ({r['href']})\n"
            result = result_str
    except ImportError:
        result = f"Search Results for '{query}': Found comprehensive details regarding '{query}'. (Mocked - duckduckgo-search not installed)"
    except Exception as e:
        result = f"Search failed: {e}"
        
    global_memory.set(f"search_{query}", result)
    return result
