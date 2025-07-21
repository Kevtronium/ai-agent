import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    if len(sys.argv) < 2:
        print("Input can't be empty. Exiting program.")
        sys.exit(1) 
    
    user_input = sys.argv[1]
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=user_input)
    print(response.text)


if __name__ == "__main__":
    main()
