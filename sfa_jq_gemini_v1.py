# /// script
# dependencies = [
#   "google-genai>=1.1.0",
# ]
# ///

import os
from google import genai

# Configure the API key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("Please set GOOGLE_API_KEY environment variable")

# Initialize the client
genai.configure(api_key=GOOGLE_API_KEY)

# Create a model instance
model = genai.GenerativeModel('gemini-1.0-pro')

# Generate text
response = model.generate_content("What is the capital of France?")

# Print the response
print("Response:", response.text)
