import os
from dotenv import load_dotenv
import pinecone
from pinecone import Pinecone

# Load environment variables from .env file at the root of the project
load_dotenv()

def init_openai_client():
    """
    Initializes the OpenAI client using the API key from the environment variable.
    Returns an instance of the ChatOpenAI client configured with the given API key.
    """
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        raise ValueError("OpenAI API key is not set in .env file.")
    
    # Adjust the initialization based on the actual library requirements.
    client = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
    return client

def init_pinecone_client():
    """
    Initializes the Pinecone client with the API key from the environment variable.
    Configures the Pinecone environment and returns the Pinecone client instance.
    """
    pinecone_api_key = os.getenv('PINECONE_API_KEY')
    if not pinecone_api_key:
        raise ValueError("Pinecone API key is not set in .env file.")
    
    # Initialize Pinecone environment
    pinecone.init(api_key=pinecone_api_key, environment='us-west1-gcp')

    # Here, you can also create or connect to an existing Pinecone index if needed.
    # Example: pinecone.Index("your-index-name")
    
    # Return the Pinecone client
    return pinecone
