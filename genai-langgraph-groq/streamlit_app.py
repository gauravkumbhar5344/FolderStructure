import streamlit as st
from auth import authenticate_user
from guardrails import ask as ask_guardrail
from tools import run_tool
from langgraph_connector import visualize_agents_mock

st.set_page_config(layout='wide', page_title='LangGraph + Groq Demo')

# Sidebar: API key and tool selection
st.sidebar.title('Settings')
api_key = st.sidebar.text_input('Groq API Key', type='password')
tool = st.sidebar.selectbox('Select tool', ['Calculator', 'Web Search (mock)'])
multi_agent = st.sidebar.radio('Agent view', ['Single Agent', 'Multi Agent'])

# Authentication
if not authenticate_user():
    st.stop()

st.title('LangGraph + Groq — Simple Demo')
col1, col2 = st.columns([2,1])

with col1:
    st.subheader('Chat')
    user_query = st.text_input('Ask a question:')
    if st.button('Send'):
        if not api_key:
            st.warning('Please provide Groq API Key in sidebar.')
        elif not user_query.strip():
            st.warning('Enter a query.')
        else:
            # Step 1: guardrail check
            try:
                decision_or_response = ask_guardrail(user_query, api_key)
            except Exception as e:
                decision_or_response = f'Guardrail/LLM call failed: {e}'
            st.markdown('**Response:**')
            st.write(decision_or_response)

    st.markdown('---')
    st.subheader('Tool Runner')
    tool_input = st.text_input('Tool input (e.g., "2+2" for Calculator or "python installation" for mock search)')
    if st.button('Run Tool'):
        try:
            output = run_tool(tool, tool_input)
        except Exception as e:
            output = f'Tool execution failed: {e}'
        st.write(output)

with col2:
    st.subheader('Multi-Agent Visualization')
    if multi_agent == 'Multi Agent':
        st.info('Multi-Agent view (visual-only mock)')
        visualize_agents_mock()
    else:
        st.info('Single Agent view (main LLM)')
        st.write('Main agent: LLaMA 3 (groq llama-3.3-70b-versatile)')
