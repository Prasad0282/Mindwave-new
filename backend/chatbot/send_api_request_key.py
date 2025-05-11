import requests
import os

# Load the API key from environment variables (if set), or directly provide it
groq_api_key = os.getenv('GROQ_API_KEY')  # Or use the key directly like 'YOUR_API_KEY'

if not groq_api_key:
    print("Error: The GROQ_API_KEY is not set.")
    exit(1)

# Set up the request headers
headers = {
    'Authorization': f'Bearer {groq_api_key}',
    'Content-Type': 'application/json',
}

# Set up the payload (the data you're sending to the API)
payload = {
    'input': 'Tell me a joke'  # Example input, replace with actual request format
}

# Send the POST request to the API
response = requests.post("https://api.groq.com/generate", json=payload, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Response from Groq API:", response.json())  # Print the response data
else:
    print(f"Error: {response.status_code} - {response.text}")  # Print error message if any