WELLNESS_APP/
│
├── agents/                # Handles all agent-specific logic
│   ├── __init__.py        # Initializes the agents package
│   ├── base_agent.py      # Base class for all agents
│   ├── memory_agent.py    # Manages retrieval of conversation memory
│   ├── dialogue_agent.py  # Handles dialogue management
│   └── summary_agent.py   # Summarizes conversation and other data
│
├── utils/                 # Utility functions and helpers
│   ├── __init__.py        # Initializes the utils package
│   ├── sentiment_analysis.py  # Sentiment analysis functionalities
│   └── medication_management.py  # Manages medication intake queries
│
├── config/                # Configuration management
│   ├── __init__.py        # Initializes the config package
│   └── settings.py        # Centralized configuration settings
│
├── services/              # External services integration
│   ├── __init__.py        # Initializes the services package
│   └── api_service.py     # API client configurations and management
│
├── interface/             # Streamlit interface for the application
│   ├── __init__.py        # Initializes the interface package
│   └── streamlit_app.py   # Streamlit application setup and UI logic
│
├── tests/                 # Unit and integration tests
│   ├── __init__.py        # Initializes the tests package
│   ├── test_memory_agent.py   # Tests for the MemoryAgent
│   ├── test_dialogue_agent.py # Tests for the DialogueAgent
│   └── test_summary_agent.py  # Tests for the SummaryAgent
│
├── .env                   # Environment variables (API keys, etc.)
├── main.py                # Main application entry point for non-Streamlit execution
└── requirements.txt       # Lists dependencies for the project
