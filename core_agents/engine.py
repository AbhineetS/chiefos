import os
import asyncio
from typing import List, Callable, Any
from pydantic import BaseModel
from google import genai
from google.genai import types

class Agent(BaseModel):
    name: str
    instructions: str
    tools: list[Callable] = []

def handoff(target_agent: Agent) -> Callable:
    """Creates a handoff tool for a specific agent."""
    def transfer_agent() -> str:
        print(f"\n[Handoff] Transferring to {target_agent.name}...")
        return target_agent  # We return the Agent object at runtime, but type hint it as str for google-genai schema.
    
    # Rename function so the LLM distinguishes multiple handoffs
    transfer_agent.__name__ = f"transfer_to_{target_agent.name.lower().replace(' ', '_')}"
    transfer_agent.__doc__ = f"Transfer the conversation to the {target_agent.name}."
    return transfer_agent

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import httpx
original_init = httpx.Client.__init__
def new_init(self, *args, **kwargs):
    kwargs['verify'] = False
    original_init(self, *args, **kwargs)
httpx.Client.__init__ = new_init

class Runner:
    @staticmethod
    async def run(starting_agent: Agent, user_input: str) -> str:
        client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
        current_agent = starting_agent
        
        # We maintain the conversation history manually so we can switch system instructions
        contents = [
            types.Content(role="user", parts=[types.Part.from_text(text=user_input)])
        ]
        
        while True:
            # We call generate_content on the current agent
            tools = current_agent.tools
            
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=contents,
                config=types.GenerateContentConfig(
                    system_instruction=current_agent.instructions,
                    tools=tools if tools else None,
                    temperature=0.0,
                )
            )
            
            # Append model's response to history
            model_parts = []
            if response.text:
                 model_parts.append(types.Part.from_text(text=response.text))
            
            if response.function_calls:
                for call in response.function_calls:
                    model_parts.append(types.Part.from_function_call(name=call.name, args=call.args))
            
            if model_parts:
                contents.append(types.Content(role="model", parts=model_parts))
                
            if not response.function_calls:
                return response.text
                 
            # Execute function calls
            function_responses = []
            agent_switched = False
            
            for call in response.function_calls:
                func = next((t for t in tools if t.__name__ == call.name), None)
                if not func:
                    function_responses.append(
                        types.Part.from_function_response(name=call.name, response={"result": "Function not found"})
                    )
                    continue
                    
                args = call.args if call.args else {}
                try:
                    import inspect
                    if inspect.iscoroutinefunction(func):
                        result = await func(**args)
                    else:
                        result = func(**args)
                        
                    if isinstance(result, Agent):
                        # Handoff detected
                        current_agent = result
                        function_responses.append(
                            types.Part.from_function_response(name=call.name, response={"result": f"Successfully transferred to {result.name}"})
                        )
                        agent_switched = True
                    else:
                        function_responses.append(
                            types.Part.from_function_response(name=call.name, response={"result": str(result)})
                        )
                except Exception as e:
                    function_responses.append(
                        types.Part.from_function_response(name=call.name, response={"error": str(e)})
                    )
            
            # Append the function responses as a user message
            contents.append(types.Content(role="user", parts=function_responses))
