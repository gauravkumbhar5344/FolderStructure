
from langgraph.graph import StateGraph, START , END
from src.langgraph_agenticai.state.state import State
from src.langgraph_agenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraph_agenticai.tools.search_tool import get_tools , create_tool_nodes
from langgraph.prebuilt import tools_condition , ToolNode
from src.langgraph_agenticai.nodes.chatbot_with_tool_node import ChatbotWithWebToolsNode



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


    def chatbot_with_tools_build_graph(self):
        """
        Builds a chatbot with web tools graph using Langgraph.
        This method initializes a chatbot node using the `ChatbotWithWebToolsNode` class
        and integrates it into te graph. The chatbot  node is set as both the entry and exit
        point of the graph.
        """
        #Defining tools and tool nodes.

        tools = get_tools()
        tool_node = create_tool_nodes(tools)
        llm = self.llm

        #Defining chatbot nodes
        obj_chatbot_with_node = ChatbotWithWebToolsNode(llm)
        chatbot_node = obj_chatbot_with_node.create_chatbot(tools)
        #Add nodes
        self.graph_builder.add_node("chatbot" , chatbot_node)
        self.graph_builder.add_node("tools" , tool_node)

        self.graph_builder.add_edge(START , "chatbot")
        self.graph_builder.add_conditional_edges("chatbot" , tools_condition)
        self.graph_builder.add_edge("tools" , "chatbot")
        self.graph_builder.add_edge("chatbot" , END)


    def setup_graph(self , usecase:str):
        """
        Sets up the graph based on the selected use case.
        Currently supports only the 'basic_chatbot' use case.
        """

        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        
        if usecase == "Chatbot With Web":
            self.chatbot_with_tools_build_graph()

        return self.graph_builder.compile()