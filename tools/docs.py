from agents.decorators import tool
from pydantic import BaseModel
import os

class ExecutiveSummary(BaseModel):
    title: str
    key_findings: list[str]
    action_items: list[str]
    summary_paragraph: str

@tool
async def generate_and_save_report(filename: str, report: ExecutiveSummary) -> str:
    """Generate a structured final report from an ExecutiveSummary object and save it to a file.
    
    Args:
        filename: The filename to save the report to (e.g. 'final_report.md')
        report: The structured ExecutiveSummary Pydantic model.
    """
    print(f"\n[Tool Execution: File Writer] Saving structured report to '{filename}'")
    
    try:
        content = f"# {report.title}\n\n"
        content += f"## Executive Summary\n{report.summary_paragraph}\n\n"
        
        content += "## Key Findings\n"
        for finding in report.key_findings:
            content += f"- {finding}\n"
            
        content += "\n## Action Items\n"
        for action in report.action_items:
            content += f"- {action}\n"
            
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
            
        return f"Successfully generated and saved structured report to {filename} in markdown format."
    except Exception as e:
        return f"Error saving report: {str(e)}"
