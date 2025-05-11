import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Package-level variable (optional)
API_KEY = os.getenv("GROQ_API_KEY")

# Make chatbot importable
from .chatbot import Chatbot
