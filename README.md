# ChiefOS

A CLI-based multi-agent application built using the `openai-agents` Python SDK.

## Features

- **Multi-Agent Architecture**: 5 specialized agents handling planning, research, meeting prep, email drafting, and report generation.
- **Agent Handoffs**: Seamless task delegation from the Executive Planner to specialized agents.
- **Human in the Loop**: Emails require explicit human approval in the terminal before "sending".
- **Structured Output**: Generates a well-formatted final report using Pydantic.
- **Shared Memory**: Cross-agent context sharing for seamless workflows.

## Setup

1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your `OPENAI_API_KEY`.

3. Run the application:
   ```bash
   python main.py
   ```

## Usage

When prompted by the CLI, enter your task. For example:
> "Research the new OpenAI Agents SDK, check my calendar for tomorrow to prep a briefing, draft an email to the team with the findings, and generate a final report."

The agents will coordinate to complete your task and prompt you for approval before sending any emails.
