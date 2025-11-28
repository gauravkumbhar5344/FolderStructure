
from src.langgraph_agenticai.state.state import State

class BasicChatbotNode:
    """"
    Basic chatbot node that can be integrated into a Langgraph graph.
    """
    def __init__(self, model):
        self.llm = model
    
    def process(self ,state:State)-> dict:
        """
        Process the input state and generate a chatbot response.
        """
        return {"message": self.llm.invoke(state['message'])}
