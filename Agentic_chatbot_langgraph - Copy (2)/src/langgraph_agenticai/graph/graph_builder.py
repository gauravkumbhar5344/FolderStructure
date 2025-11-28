
from langgraph.graph import StateGraph, START , END
from src.langgraph_agenticai.state.state import State
from src.langgraph_agenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraph_agenticai.nodes.ai_news_node import AINewsNode




class GraphBuilder:
    def __init__(self , model):
        self.llm = model
        self.graph_builder = StateGraph(State)


    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using Langgraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class
        and integrates it into te graph. The chatbot  node is set as both the entry and exit
        point of the graph.
        """

        self.basic_chatbot_node = BasicChatbotNode(self.llm)

 

        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START , "chatbot")
        self.graph_builder.add_edge("chatbot" , END)



    def ai_news_build_graph(self):
        """
        Builds an AI News graph using Langgraph.
        This method initializes nodes specific to the AI News use case
        and integrates them into the graph. The nodes are connected to form
        a coherent flow from start to end.
        """
        ai_news_node = AINewsNode(self.llm)

    # Add the correct nodes and edges for the AI News use case
        self.graph_builder.add_node("fetch_news", ai_news_node.fetch_news)
        self.graph_builder.add_edge("fetch_news", "summarize_news")  # Corrected edge
        self.graph_builder.add_node("summarize_news", ai_news_node.summarize_news)  # Added missing node for summarize_news
        self.graph_builder.add_edge("summarize_news", "save_result")  # Corrected edge
        self.graph_builder.add_node("save_result", ai_news_node.save_result)  # Added missing node for save_result
        self.graph_builder.add_edge("save_result", END)

    # Set the entry point for the graph
        self.graph_builder.set_entry_point("fetch_news")


    def setup_graph(self , usecase:str):
        """
        Sets up the graph based on the selected use case.
        Currently supports only the 'basic_chatbot' use case.
        """

        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        if usecase == "AI News":
            self.ai_news_build_graph()

        return self.graph_builder.compile()