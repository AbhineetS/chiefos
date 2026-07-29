# ChiefOS

A CLI-based multi-agent application built using the official `google-genai` Python SDK.

## Features

- **Multi-Agent Architecture**: 5 specialized agents handling planning, research, meeting prep, email drafting, and report generation.
- **Agent Handoffs**: Seamless task delegation from the Executive Planner to specialized agents.
- **Human in the Loop**: Emails require explicit human approval in the terminal before "sending".
- **Structured Output**: Generates a well-formatted final report using Pydantic.
- **Shared Memory**: Cross-agent context sharing for seamless workflows.
- **Graceful Error Handling**: Validates environment and handles missing keys without crashing.
- **Real Search Integration**: Uses DuckDuckGo to perform real web searches.

## Setup Instructions

1. **Create virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create .env**:
   ```bash
   cp .env.example .env
   ```
   *Note: If you skip this step, running the app will automatically create the `.env` file for you.*

4. **Add GEMINI_API_KEY**:
   Open `.env` in your text editor and add your actual Google Gemini API Key.
   ```
   GEMINI_API_KEY=AIza...
   ```

5. **Run project**:
   ```bash
   python main.py
   ```

## Usage

When prompted by the CLI, enter your task. For example:
> "Research the new OpenAI Agents SDK, check my calendar for tomorrow to prep a briefing, draft an email to the team with the findings, and generate a final report."

The agents will coordinate to complete your task and prompt you for approval before sending any emails.
