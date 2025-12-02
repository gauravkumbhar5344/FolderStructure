
from src.langgraph_agenticai.state.state import State

class ChatbotWithWebToolsNode:
    """A chatbot node that utilizes web tools for enhanced responses."""

    def __init__(self, llm):
        self.llm = llm

    def process(self, state: State) -> dict:
        """Processes the input state and generates a response using web tools."""
        user_input = state["message" ][-1] if state["message"] else ""
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])

        #simulate toolspecigic logic

        tool_response = f"Tool integraion for: '{user_input}'"

        return {"messages": [llm_response ,tool_response]}
    

    def create_chatbot(self , tools):
        """chatbot logic for processing the input state and generating a response."""

        llm_with_tools = self.llm.bind_tools(tools)
        
        def chatbot_node(state: State):
            return {"messages": [llm_with_tools.invoke(state["message"])]}

        return chatbot_node