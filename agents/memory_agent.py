from .base_agent import BaseAgent
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class MemoryAgent(BaseAgent):
    """
    An agent that retrieves relevant parts of the conversation history
    based on the user's query.
    """
    def __init__(self, client):
        super().__init__(client)
        self.memory_handler_template = """
        You are an agent that retrieves conversation history  {conversation_history}
        and summarizes it according to the user query {query}.
        You will return exclusively those elements of the conversation history which are relevant to the query.
        The content you provide should be included in the conversation history; you should not add anything else to it.
        you will output a Json output:
        (
            "relevant_memory": summary of the history in relation to the query
        )
        """
        self.prompt_memory_handler = PromptTemplate(
            template=self.memory_handler_template,
            input_variables=["query", "conversation_history"]
        )

    def handle_memory(self, query, conversation_history):
        """
        Retrieves relevant parts of the conversation history based on the user's query.

        :param query: User's query as a string.
        :param conversation_history: The conversation history as a list of dialogue turns.
        :return: A subset of the conversation history relevant to the query.
        """
        prompt_data = {'query': query, "conversation_history": conversation_history}
        try:
            relevant_memory = LLMChain(
                prompt=self.prompt_memory_handler,
                llm=self.client
            ).run(prompt_data)
            return relevant_memory
        except Exception as e:
            print(f"Error parsing memory: {e}")
            return []


