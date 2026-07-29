import asyncio
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

def dummy_tool():
    """Dummy tool."""
    pass

async def main():
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    contents = [types.Content(role="user", parts=[types.Part.from_text(text="Call dummy tool")])]
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(tools=[dummy_tool], temperature=0.0)
    )
    print(response.function_calls)
    
    model_parts = []
    for call in response.function_calls:
        model_parts.append(types.Part.from_function_call(name=call.name, args=call.args))
    contents.append(types.Content(role="model", parts=model_parts))
    
    function_responses = []
    for call in response.function_calls:
        function_responses.append(types.Part.from_function_response(name=call.name, response={"result": "OK"}))
    contents.append(types.Content(role="user", parts=function_responses))
    
    try:
        res2 = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=contents,
            config=types.GenerateContentConfig(tools=[dummy_tool], temperature=0.0)
        )
        print("Success")
    except Exception as e:
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
