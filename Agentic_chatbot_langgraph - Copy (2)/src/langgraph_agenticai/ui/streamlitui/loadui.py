
import streamlit as st
import os
from src.langgraph_agenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}
    
    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")
        st.title(self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False

        with st.sidebar:
            #Get Options from config file
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            #LLM Selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM" , llm_options)

            #Model Selection
            if self.user_controls["selected_llm"] == "Groq":
                #Model Selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model" , model_options)
                self.user_controls["GRPQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("Enter GROQ API Key" , type="password")

                #Validate API Key
                if not self.user_controls["GRPQ_API_KEY"]:
                    st.warning("Please enter a valid GROQ API Key to proceed.")
                
            #Usecase Selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecase" , ["Basic Chatbot", "Chatbot With Web", "AI News"])

            if self.user_controls["selected_usecase"] == "AI News":
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("Enter TAVILY API Key" , type="password")
                #Validate API Key
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("Please enter a valid TAVILY API Key to proceed.")
                    
            if self.user_controls["selected_usecase"] == "AI News":
                st.subheader("AI News Settings")

                with st.sidebar:
                    time_frame = st.selectbox(
                        "Select Time Frame",
                        ["Daily", "Weekly", "Monthly"],
                        index=0
                    )
                
                if st.button("Fetch Latest News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeframe = time_frame

        return self.user_controls
    
            