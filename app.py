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
# Load environment variables
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
pinecone_api_key = os.getenv('PINECONE_API_KEY')

# Initialize Pinecone and OpenAI clients
client = OpenAI(model_name="gpt-3.5-turbo", temperature=0)
pc = Pinecone(api_key=pinecone_api_key)
index_name = 'yogasutra'

# Initialize agents
memory_agent = MemoryAgent(client)
dialogue_agent = DialogueAgent(client)
summary_agent = SummaryAgent(client)

# Streamlit setup
st.title("Interactive Conversation Agent")
st.sidebar.header("Agent Controls")
run_summary = st.sidebar.checkbox("Generate summary after conversation", True)
medications = st.sidebar.text_input("Enter medications to track, separated by commas").split(',')

# Managing conversation history
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

# User input
user_input = st.text_input("Enter your query (type 'exit' to end the session):", key="query_input")

if user_input.lower() == 'exit':
    if run_summary and st.session_state.conversation_history:
        st.write("Please review your medication intake:")
        intake_table = ask_about_medication(medications, interface='streamlit')
        if st.button("Generate Summary"):
            # Sentiment analysis and medication summary
            mental_status = [SentimentIntensityAnalyzer().polarity_scores(item['user']) for item in st.session_state.conversation_history]
            summary = summary_agent._run_summary(mental_status, st.session_state.conversation_history, intake_table)
            st.write("Conversation Summary:", summary)
            st.session_state.conversation_history = []  # Clear conversation history after processing
            st.stop()
    else:
        st.stop()

if st.button("Send"):
    index = pc.Index(index_name)
    index.describe_index_stats()
    context,tracking = retrieve(user_input, limit=500, k=5)

    # Memory retrieval
    relevant_memory = memory_agent.handle_memory(user_input, st.session_state.conversation_history)

    # Run dialogue
    response = dialogue_agent._run_dialogue(user_input, relevant_memory, context)
    st.session_state.conversation_history.append({"user": user_input, "bot": response})
    st.write("Response:", response)
    st.write("Tracking:", tracking)

# Display the current conversation history
st.write("Conversation History:")
for turn in st.session_state.conversation_history:
    st.text(f"User: {turn['user']}")
    st.text(f"Bot: {turn['bot']}")
