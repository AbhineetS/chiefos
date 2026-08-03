# Demo Video Recording Script (5–10 Minutes)

## Preparation (Before Recording)
1. Ensure your `.env` file is set up with a valid `GEMINI_API_KEY`.
2. Open your terminal and activate the virtual environment (`source .venv/bin/activate`).
3. Have your IDE (VS Code / Cursor) open in the background so you can briefly show the code.
4. Have this script ready off-screen.

---

## 1. Introduction (0:00 - 1:00)
- **Visual**: Camera on you (optional) or screen showing the project README.
- **Script**: "Hi, my name is [Your Name], and this is my academic project: ChiefOS. ChiefOS is a virtual AI Chief of Staff built using the Google Gemini SDK. It is a multi-agent system designed to help executives automate their research, schedule checking, and email drafting. Today, I'm going to walk you through the architecture and do a live demonstration."

## 2. Architecture Overview (1:00 - 2:30)
- **Visual**: Switch to your IDE. Briefly show `core_agents/planner.py` and `core_agents/engine.py`.
- **Script**: "The core of the system uses a Hub-and-Spoke architecture. We have an Executive Planner agent that acts as the router. It receives the user's prompt and delegates tasks to 5 specialized agents: a Research Analyst, a Meeting Prep agent, a Strategy Tracker, an Email Manager, and a Report Generator. 
We handle the agent handoffs dynamically by passing functions as tools to the Gemini API. Crucially, we also handle API rate limiting in `engine.py` with an exponential backoff retry loop, ensuring the application is resilient."

## 3. The Live Demo Setup (2:30 - 3:00)
- **Visual**: Open your terminal. Run `python main.py`. 
- **Script**: "Let's run it. I'm going to give ChiefOS a complex, multi-step prompt that requires all the agents to work together."
- **Action**: Paste the following prompt into the terminal: 
  > *Research the new OpenAI Agents SDK, check my calendar for tomorrow to prep a briefing, draft an email to the team with the findings, and generate a final report.*

## 4. Execution & Handoffs (3:00 - 6:00)
- **Visual**: The terminal will start printing `[Handoff] Transferring to...` and `[Tool Execution...]`. 
- **Script**: "You can see the Executive Planner immediately transferred control to the Research Analyst, which triggered the Web Search tool. Next, it hands off to the Meeting Prep agent to check my calendar. Behind the scenes, these agents are saving their findings into a shared Global Memory key-value store, which prevents us from blowing up the LLM's context window."
- *(If the rate limit retry triggers)*: "Notice here we hit a 429 Rate Limit error from the Gemini free tier. Our custom engine catches this and gracefully sleeps, proving our error handling is robust."

## 5. Human-in-the-Loop Approval (6:00 - 7:30)
- **Visual**: The terminal pauses at `>>> Approve this email for sending? (y/n):`.
- **Script**: "A critical feature of ChiefOS is safety. Autonomous agents shouldn't blindly send emails. Here, the Email Manager has drafted the email based on the research, but it halts execution to ask for human approval. This proves our Human-in-the-Loop requirement."
- **Action**: Type `y` and hit Enter.

## 6. Structured Output (7:30 - 8:30)
- **Visual**: The terminal finishes execution. Show the newly created `final_report.md` file in the IDE.
- **Script**: "Finally, the Report Generator synthesizes everything. Using Pydantic structured output models, we force the LLM to return exactly the JSON schema we need, which we then format into this markdown file. As you can see, we have the Executive Summary, Key Findings, and Action Items perfectly formatted."

## 7. Conclusion (8:30 - 9:00)
- **Visual**: Back to terminal or camera.
- **Script**: "In conclusion, ChiefOS successfully fulfills all requirements: 6 specialised agents, 5 integrated tools, seamless handoffs, human-in-the-loop safety, and structured outputs. Thank you for watching!"
