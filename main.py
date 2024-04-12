import streamlit as st
import os
from dotenv import load_dotenv
from agents.memory_agent import MemoryAgent
from agents.dialogue_agent import DialogueAgent
from agents.summary_agent import SummaryAgent
from services.api_service import *
from utils.sentiment_analysis import SentimentIntensityAnalyzer
from utils.medication_management import ask_about_medication
from pinecone import Pinecone
from utils.retriever import retrieve
from langchain.llms import OpenAI

# Load environment variables
import os
from dotenv import load_dotenv
from agents.memory_agent import MemoryAgent
from agents.dialogue_agent import DialogueAgent
from agents.summary_agent import SummaryAgent
from services.api_service import *
from utils.sentiment_analysis import SentimentIntensityAnalyzer
from utils.medication_management import ask_about_medication
from pinecone import Pinecone
from utils.retriever import retrieve
from langchain_openai import OpenAI
from langchain import  OpenAI




load_dotenv()



openai_api_key = os.getenv('OPENAI_API_KEY')
print(openai_api_key)
client = OpenAI(model_name="gpt-3.5-turbo", temperature=0)


pinecone_api_key = os.getenv('PINECONE_API_KEY')
pc = Pinecone(api_key=pinecone_api_key)
    # Initialize agents
memory_agent = MemoryAgent(client)
dialogue_agent = DialogueAgent(client)
summary_agent = SummaryAgent(client)

    # Example conversation history
conversation_history = []
index_name='yogasutra'
    # Main loop for dialogue interaction
while True:
        index = pc.Index(index_name)
        index.describe_index_stats()
        user_input = input("\nEnter your query (or type 'exit' to stop): ")
        if user_input.lower() == 'exit':
            break
        context=retrieve(user_input, limit=500,k=5)
        print('Context',context)
        # # Placeholder for context retrieval logic

        # Memory retrieval
        relevant_memory = memory_agent.handle_memory(user_input, conversation_history)
        print("Relevant Memory:", relevant_memory)

        # Run dialogue
        response = dialogue_agent._run_dialogue(user_input, relevant_memory, context)
        print("Bot:", response)

        # Update conversation history
        conversation_history.append({"user": user_input, "bot": response})

    # Post-conversation summary (optional)
    # This could involve sentiment analysis and medication intake summary
    # Example placeholder for sentiment analysis
mental_status = [SentimentIntensityAnalyzer().polarity_scores(item['user']) for item in conversation_history]
print('Mental Status', mental_status)
intake_table = ask_about_medication(["Aspirin", "Purpurin"])
summary = summary_agent._run_summary(mental_status, conversation_history, intake_table)
print("\nConversation Summary:", summary)