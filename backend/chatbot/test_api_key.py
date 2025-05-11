import os

# Get the environment variable value
groq_api_key = os.getenv('GROQ_API_KEY')

# Print the result to verify if it's loaded correctly
if groq_api_key:
    print("GROQ_API_KEY is set:", groq_api_key)
else:
    print("GROQ_API_KEY is NOT set.")