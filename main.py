import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content

def print_response(response, user_prompt, verbose=False):
    function_calls = response.function_calls

    if function_calls:
        for function_call in function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")

    print("Response: ")
    print(response.text)
    if verbose:
        print(f"User prompt: ", user_prompt)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    

def main():
    load_dotenv()

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a TODO List app?"')
        sys.exit(1) 
        
    user_prompt = args[0]
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    verbose_flag = False

    if "--verbose" in sys.argv:
        verbose_flag = True
    
    available_functions = types.Tool(function_declarations=[schema_get_files_info, schema_get_file_content])
    config = types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages, config=config)
    print_response(response, user_prompt, verbose_flag)


if __name__ == "__main__":
    main()
