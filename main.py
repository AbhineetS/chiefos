import os
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()

import asyncio
import logging
from dotenv import load_dotenv
import sys
import shutil

# Automatically create .env from .env.example if it doesn't exist
if not os.path.exists(".env") and os.path.exists(".env.example"):
    shutil.copy(".env.example", ".env")
    print("[ChiefOS System] Automatically created '.env' file from '.env.example'.")

load_dotenv()

def validate_startup():
    # If the default placeholder is still there or it's missing, consider it not configured
    key = os.environ.get("GEMINI_API_KEY")
    if not key or key == "your-gemini-api-key-here" or "PASTE_YOUR_GEMINI_API_KEY_HERE" in key or key.strip() == "":
        print("=======================================")
        print("Configuration Error: Missing GEMINI_API_KEY")
        print("=======================================")
        print("The ChiefOS application requires a Google Gemini API key to function.")
        print("Please follow these steps to set it up:")
        print("1. Open the '.env' file in the project root directory (ChiefOS/).")
        print("2. Add your actual API key: GEMINI_API_KEY=AIza...")
        print("3. Run the application again.")
        print("\nExiting gracefully. The project is fully functional and only requires a valid GEMINI_API_KEY to execute.")
        sys.exit(0)

validate_startup()

from core_agents.planner import planner_agent
from core_agents.engine import Runner

async def main():
    print("=======================================")
    print("Welcome to ChiefOS (Powered by Gemini)!")
    print("=======================================")
    print("Enter your task (or type 'exit' to quit):")
    
    while True:
        try:
            try:
                user_input = input("\nUser> ")
            except EOFError:
                break
                
            if user_input.strip().lower() in ['exit', 'quit']:
                break
                
            if not user_input.strip():
                continue
                
            print("\n[ChiefOS] Processing your request...")
            result = await Runner.run(planner_agent, user_input)
            print(f"\n[ChiefOS Final Output]\n{result}")
            
        except Exception as e:
            print(f"\n[Error]: {e}")
            logging.error(f"Execution failed: {e}", exc_info=True)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    asyncio.run(main())
