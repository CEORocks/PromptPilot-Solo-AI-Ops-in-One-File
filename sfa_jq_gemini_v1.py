# /// script
# dependencies = [
#   "google-genai>=1.1.0",
# ]
# ///

import os
import sys
import argparse
from google import genai

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate text using Gemini API')
    parser.add_argument('prompt', nargs='?', default="What is the capital of France?",
                      help='The prompt to send to Gemini (default: "What is the capital of France?")')
    args = parser.parse_args()

    # Configure the API key
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    if not GEMINI_API_KEY:
        print("Error: GEMINI_API_KEY environment variable is not set")
        print("Please get your API key from https://makersuite.google.com/app/apikey")
        print("Then set it with: export GEMINI_API_KEY='your-api-key-here'")
        sys.exit(1)

    # Initialize client
    client = genai.Client(api_key=GEMINI_API_KEY, http_options={"api_version": "v1alpha"})

    try:
        # Generate text
        print(f"\nPrompt: {args.prompt}")
        response = client.models.generate_content(
            model="gemini-2.0-flash-001", 
            contents=args.prompt
        )
        print("\nResponse:", response.text)

    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
