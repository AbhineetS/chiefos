from agents import Agent
from tools.search import web_search
from tools.pdf import extract_text_from_pdf

research_agent = Agent(
    name="Research Analyst",
    instructions=(
        "You are a meticulous research analyst. "
        "Use the web search tool to find information, or the PDF reader to extract information from documents. "
        "Always summarize your findings clearly and concisely so that other agents can understand them."
    ),
    tools=[web_search, extract_text_from_pdf],
)
