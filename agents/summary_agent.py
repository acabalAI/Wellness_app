from .base_agent import BaseAgent
from .base_agent import BaseAgent
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class SummaryAgent(BaseAgent):
    def __init__(self, client):
        # Initialize only BaseAgent, as MemoryHandler is not directly inherited
        super().__init__(client)


    def _run_summary(self,mental_status,relevant_memory,intake_table):
        # Note: You need to provide the context to this method or generate it within the method
        self.mental_status=mental_status
        self.relevant_memory=relevant_memory
        self.intake_table=intake_table


        self.summary_manager = """
            You are an agent that will summarise the dialogue of user based on :
            1- mental_status {mental_status} based on the utterances of the user using VADER
            2- the memory of the dialogue of the user answer questionsa about the yoga sutra, you will outline the main points {relevant_memory}
            3- situtation of the drug intake {intake_table} based on the level of completion of the prescribed intake as per
            the table {intake_table}, highlighting those drugs not taken by the user.
            
        """

        self.prompt_summary_manager = PromptTemplate(template=self.summary_manager, input_variables=["mental_status", "relevant_memory", "intake_table"])

        try:
            self.llm_chain_summary_manager = LLMChain(prompt=self.prompt_summary_manager, llm=self.client)
            response = self.llm_chain_summary_manager.run({'mental_status': self.mental_status, 'relevant_memory': self.relevant_memory, 'intake_table': self.intake_table})
            return response
        except Exception as e:
            print(e)
            return "Error managing the summary"