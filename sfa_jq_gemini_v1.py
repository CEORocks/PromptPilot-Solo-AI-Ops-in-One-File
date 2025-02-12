# /// script
# dependencies = [
#   "google-genai>=1.1.0",
# ]
# ///

import os
import sys
from google import genai

def main():
    # Configure the API key
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    if not GOOGLE_API_KEY:
        print("Error: GOOGLE_API_KEY environment variable is not set")
        print("Please get your API key from https://makersuite.google.com/app/apikey")
        print("Then set it with: export GOOGLE_API_KEY='your-api-key-here'")
        sys.exit(1)

    try:
        # Initialize the client
        genai.configure(api_key=GOOGLE_API_KEY)

        # Create a model instance
        model = genai.GenerativeModel('gemini-1.0-pro')

        # Generate text
        prompt = "What is the capital of France?"
        print(f"\nPrompt: {prompt}")
        
        response = model.generate_content(prompt)
        print("\nResponse:", response.text)

    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
