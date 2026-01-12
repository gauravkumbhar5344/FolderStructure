import streamlit as st
from src.langgraph_agenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraph_agenticai.LLMS.groqllm import GroqLLM
from src.langgraph_agenticai.graph.graph_builder import GraphBuilder
from src.langgraph_agenticai.ui.streamlitui.display_result import DisplayResultStreamlit

from src.guardrails.guardrails import guardrail_ask, load_guardrail_models

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph Agentic AI application with streamlit UI.
    This function initializes the UI components and handles user interactions, configures the LLM model,
    sets up th graph based on the selected use case, and displays the output while implementing
    exception handling for robustness.
    """

    #Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Failed to load user inputs from the UI.")
        return

    user_message = st.chat_input("Enter your message here:")


    if user_message:
        try:
            #Configure the LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error : Failed to initialize the LLM model.")
                return
            
            #Setup the graph based on use case
            g_key = "GROQ_API_KEY"
            guardrail_llm = load_guardrail_models(g_key)
            st.write("🔒 Running Guardrails...")

            guard_output = guardrail_ask(user_message, model , guardrail_llm)

            if "❌" in guard_output:
                st.error(guard_output)
                return


            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("Error: No use case selected.")
                return

            #Graph Builder 
            graph_builder = GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph , user_message).display_result_on_ui()

            except ValueError as e:
                st.error(f"Error : Graph setup failed with exception: {e}")
                return


        except Exception as e:
            st.error(f"An error occurred while processing your request: {e}")

            return
