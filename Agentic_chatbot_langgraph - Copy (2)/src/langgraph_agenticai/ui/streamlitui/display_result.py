
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage , ToolMessage
import json
#from src.langgraph_agenticai.LLMS import get_llm_model

class DisplayResultStreamlit:
    def __init__(self ,usecase ,graph , user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        if usecase == "Basic Chatbot":
            for event in graph.stream({"message": ("user", user_message)}):
                print(event.values())
                for value in event.values():
                    print(value['message'])
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        st.write(value['message'].content)

        elif usecase == "AI News":
            frquency = self.user_message
            print(frquency , type(frquency))
            with st.spinner("Fetching and summarizing news..."):
                result = graph.invoke({"message": frquency})
                st.write(result)
                print(result)
                try:
                    #Read the markdown file
                    AI_NEWS_PATH = f"./AINews/{frquency.lower()}_summary.md"
                    with open(AI_NEWS_PATH, 'r') as file:
                        markdown_content = file.read()
                    
                    st.markdown(markdown_content , unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error("Summary file not found. Please ensure the news summary was generated correctly.")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")