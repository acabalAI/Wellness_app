import openai
from pinecone import Pinecone
import os
from dotenv import load_dotenv
index_name='yogasutra'

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
pinecone_api_key = os.getenv('PINECONE_API_KEY')
pc = Pinecone(api_key=pinecone_api_key)

pc = Pinecone(api_key=pinecone_api_key)

index = pc.Index(index_name)
def retrieve(query, limit=500,k=5,embed_model= "text-embedding-ada-002"):
    res = openai.Embedding.create(
        input=[query],
        engine=embed_model
    )

    # Retrieve from Pinecone
    xq = res['data'][0]['embedding']

    # Get relevant contexts
    res = index.query(vector=xq, top_k=k, include_metadata=True)
    contexts = [x['metadata']['text'] for x in res['matches']]
    tracker=[x['metadata'] for x in res['matches']]

    # Initialize variables to build the prompt with retrieved contexts included
    selected_contexts = []
    total_tokens = 0

    # Token counting function (this is a placeholder, you might need a specific implementation)
    def count_tokens(text):
        return len(text.split())

    # Append contexts until hitting the token limit
    for context in contexts:
        context_tokens = count_tokens(context)
        if total_tokens + context_tokens <= limit:
            selected_contexts.append(context)
            total_tokens += context_tokens
        else:
            # Stop adding contexts if the next one would exceed the limit
            break

    clean_contexts = [context.replace('\n', ' ').strip() for context in selected_contexts]

    # Optionally, normalize spaces in each cleaned string
    clean_contexts = [' '.join(context.split()) for context in clean_contexts]

    # If you need a single string result
    clean_text = ' '.join(clean_contexts)
    return clean_text,tracker
