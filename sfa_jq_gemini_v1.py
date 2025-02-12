# /// script
# dependencies = [
#   "google-genai>=1.1.0",
# ]
# ///

from google import genai

client = genai.GenerativeModel("gemini-2.0-flash-001")

response = client.generate_content("What is the capital of France?")
print(response.text)
