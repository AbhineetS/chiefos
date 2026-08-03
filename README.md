# ChiefOS: The Virtual AI Chief of Staff

ChiefOS is a multi-agent executive assistant built with the official `google-genai` Python SDK. It acts as a central hub for automating complex executive operations, seamlessly delegating tasks to a team of specialized AI agents to research, plan, track strategy, and draft communications.

## 🌟 Key Project Features (Fulfilling Academic Requirements)

### 1. Multi-Agent Architecture
ChiefOS implements a Hub-and-Spoke architecture with **6 specialized AI agents**:
- **Executive Planner**: Orchestrates task delegation.
- **Research Analyst**: Conducts real-time web searches.
- **Meeting Preparation**: Parses calendar events.
- **Strategy Tracker**: Monitors high-level company OKRs.
- **Email Manager**: Drafts outbound executive communications.
- **Report Generator**: Synthesizes structured markdown summaries.

*See [`docs/architecture_design.md`](docs/architecture_design.md) for the architecture diagram and handoff flow.*

### 2. Tool Integration
The agents are empowered by Python tools to interact with external data:
1. `web_search` (DuckDuckGo integration)
2. `get_upcoming_meetings` (Calendar parsing)
3. `get_company_okrs` (Strategy tracking)
4. `draft_and_send_email` (Outbound comms)
5. `generate_and_save_report` (File I/O)
6. `extract_text_from_pdf` (RAG / Document reading)

### 3. Advanced AI Capabilities
- **Human-in-the-Loop**: Absolute safety is maintained by hard-stopping execution to prompt the human operator via the terminal (`y/n`) before outbound emails are actually sent.
- **Memory & Context Management**: To prevent LLM context-window pollution, agents share data via a centralized `global_memory` Key-Value store. 
- **Structured Outputs**: The Report Generator utilizes Pydantic data models (`ExecutiveSummary`) to guarantee the LLM returns strictly formatted JSON.
- **Error Handling & API Resilience**: Complex agent networks rapidly consume API rate limits (like Gemini's 15 RPM). The custom `Runner` engine intercepts `429 RESOURCE_EXHAUSTED` errors and applies an exponential backoff retry loop to ensure execution succeeds gracefully.

## 📁 Project Documentation
- **[Problem Analysis](docs/problem_analysis.md)**: Business context and objectives.
- **[Architecture & Design](docs/architecture_design.md)**: Mermaid diagram and interaction flow.
- **[Presentation Slides](docs/presentation_slides.md)**: 12-slide presentation outline for defense.
- **[Demo Script](docs/demo_script.md)**: Step-by-step 5-10 minute video demonstration script.

## 🚀 Setup Instructions

1. **Create virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**:
   Create a `.env` file and add your Google Gemini API Key.
   ```
   GEMINI_API_KEY=AIza...
   ```

4. **Run the Project**:
   ```bash
   python main.py
   ```

## 💻 Usage Example

When prompted by the CLI, enter a complex multi-part task:
> "Research the new OpenAI Agents SDK, check my calendar for tomorrow to prep a briefing, draft an email to the team with the findings, and generate a final report."

The Executive Planner will take over, delegating sub-tasks across the specialized agents, halting for your approval before emailing, and finally saving a synthesized `.md` file to the directory.
