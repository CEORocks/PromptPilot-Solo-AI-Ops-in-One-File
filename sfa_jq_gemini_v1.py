# /// script
# dependencies = [
#   "google-genai>=1.1.0",
# ]
# ///

import os
import sys
from google import genai

# Configure the API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("Error: GEMINI_API_KEY environment variable is not set")
    sys.exit(1)

client = genai.Client(api_key=GEMINI_API_KEY, http_options={"api_version": "v1alpha"})


def main():

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", contents="What is the capital of France?"
    )

    print("\nResponse:", response.text)


if __name__ == "__main__":
    main()
