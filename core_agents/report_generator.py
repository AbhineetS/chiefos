from agents import Agent
from tools.docs import generate_and_save_report

report_generator_agent = Agent(
    name="Report Generator",
    instructions=(
        "You are the Report Generator. "
        "You compile all information and findings from the workflow into a structured executive summary. "
        "Always use the generate_and_save_report tool to save the final output to a markdown file (e.g., 'final_report.md')."
    ),
    tools=[generate_and_save_report],
)
