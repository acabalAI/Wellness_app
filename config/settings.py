from dotenv import load_dotenv
import os
import openai

# Load environment variables from a .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Example additional configurations
MODEL_NAME = 'gpt-3.5-turbo'

openai.proxy = {
            "http": "http://127.0.0.1:7890",
            "https": "http://127.0.0.1:7890"
       }

