from core_agents.engine import Agent, handoff
from core_agents.research import research_agent
from core_agents.meeting_prep import meeting_prep_agent
from core_agents.email_manager import email_manager_agent
from core_agents.report_generator import report_generator_agent
from core_agents.strategy_tracker import strategy_tracker_agent

planner_agent = Agent(
    name="Executive Planner",
    instructions="""You are the Executive Planner, the central orchestrator of ChiefOS.
Your job is to break down the user's task and delegate subtasks to the appropriate specialized agents.
Use the transfer tools to handoff the conversation to a specialist. 
When a specialist finishes, they will transfer back to you with their results.
Keep delegating until the entire task is complete.
Once the entire task is fully complete, summarize the final outcome to the user and stop.
Do not make up information; always rely on the specialists.
""",
    tools=[
        handoff(research_agent),
        handoff(meeting_prep_agent),
        handoff(email_manager_agent),
        handoff(report_generator_agent),
        handoff(strategy_tracker_agent)
    ]
)

# We must add the transfer_to_executive_planner tool to the specialists now that planner_agent is defined
transfer_to_planner = handoff(planner_agent)
research_agent.tools.append(transfer_to_planner)
meeting_prep_agent.tools.append(transfer_to_planner)
email_manager_agent.tools.append(transfer_to_planner)
report_generator_agent.tools.append(transfer_to_planner)
strategy_tracker_agent.tools.append(transfer_to_planner)
