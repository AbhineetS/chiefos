import asyncio
import logging
from dotenv import load_dotenv

load_dotenv()

from agents import Runner, RunState
from core_agents.planner import planner_agent

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

async def confirm(question: str) -> bool:
    """Prompt user for yes/no confirmation in the CLI."""
    while True:
        response = input(f"{question} (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        print("Please enter 'y' or 'n'.")

async def main():
    print("=======================================")
    print("Welcome to ChiefOS MVP!")
    print("=======================================")
    print("Type your task below (or 'exit' to quit):\n")
    
    while True:
        try:
            user_input = input("\nUser> ")
            if user_input.lower() in ['exit', 'quit']:
                break
                
            if not user_input.strip():
                continue
                
            print("\nStarting workflow...")
            
            result = await Runner.run(
                planner_agent,
                user_input,
            )
            
            # Handle human-in-the-loop tool approvals
            has_interruptions = len(result.interruptions) > 0
            while has_interruptions:
                print("\n" + "=" * 80)
                print("Run interrupted - Tool approval required")
                print("=" * 80)
                
                state = result.to_state()
                
                for interruption in result.interruptions:
                    print("\nTool call details:")
                    print(f"  Agent: {interruption.agent.name}")
                    print(f"  Tool: {interruption.name}")
                    print(f"  Arguments: {interruption.arguments}")
                    
                    confirmed = await confirm("\nDo you approve this action?")
                    
                    if confirmed:
                        print(f"✓ Approved: {interruption.name}")
                        state.approve(interruption)
                    else:
                        print(f"✗ Rejected: {interruption.name}")
                        state.reject(interruption)
                
                print("\nResuming agent execution...")
                result = await Runner.run(planner_agent, state)
                has_interruptions = len(result.interruptions) > 0
            
            print("\n" + "=" * 80)
            print("Final Output:")
            print("=" * 80)
            print(result.final_output)
            
        except Exception as e:
            logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())
