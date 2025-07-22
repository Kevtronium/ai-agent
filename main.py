import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def print_response(response, user_prompt, verbose=False):
    print("Response: ")
    print(response.text)
    if verbose:
        print(f"User prompt: ", user_prompt)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

def main():
    load_dotenv()

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
        
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    print_response(response, user_prompt, verbose_flag)


if __name__ == "__main__":
    main()
