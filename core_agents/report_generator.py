from core_agents.engine import Agent, handoff
from tools.docs import generate_and_save_report

report_generator_agent = Agent(
    name="Report Generator",
    instructions="""You are the Report Generator.
Your job is to compile the final findings into a beautiful, structured markdown report.
Use the generate_and_save_report tool to create and save the final report.
Once the report is saved, transfer back to the Executive Planner.
You must always use the transfer_to_executive_planner tool when finished.
""",
    tools=[generate_and_save_report]
)
