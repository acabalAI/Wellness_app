# dialogue_agent.py in the agents/ directory

from .base_agent import BaseAgent
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class DialogueAgent(BaseAgent):
    def __init__(self, client):
        super().__init__(client)
        self.dialogue_manager_template = """
            You are a dialogue agent based on the Yoga Sutras of Patanjali. Given a query {query} and the context {context},
            along with the relevant history of the conversation {relevant_memory}, keep track of the dialogue thread.
            Answer the query using the context and use the history of the conversation to follow up on the dialogue thread,
            ensuring it remains aligned. Only answer questions related to the Yoga Sutra,
            and use the content in the {context} and {relevant_memory} to answer them,
            in the otherwise, say,"Sorry, this is out of the scope of my knowledge."
        """
        self.prompt_template = PromptTemplate(
            template=self.dialogue_manager_template,
            input_variables=["query", "relevant_memory", "context"]
        )

    def _run_dialogue(self, query, relevant_memory, context):
        # Here, context is assumed to be generated or provided by another part of the system.
        self.query = query
        self.relevant_memory = relevant_memory
        self.context = context

        try:
            llm_chain_dialogue_manager = LLMChain(prompt=self.prompt_template, llm=self.client)
            response = llm_chain_dialogue_manager.run({
                'query': self.query,
                'relevant_memory': self.relevant_memory,
                'context': self.context
            })
            return response
        except Exception as e:
            print(f"Error managing the conversational flow: {e}")
            return "Sorry, I encountered an error processing your request."

