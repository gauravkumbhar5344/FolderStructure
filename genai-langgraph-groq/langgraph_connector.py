import streamlit as st

def visualize_agents_mock():
    # Simple visual mockup to represent agents and connections
    st.write('Agents:')
    st.markdown('''
    - **Guardrail Agent** — checks safety (groq/compound-mini)
    - **Main Agent** — answers allowed queries (llama-3.3-70b-versatile)
    - **Tool Agent** — executes selected tool (Calculator / WebSearch)
    ''')
    st.markdown('''
    ```
    [User] --> [Guardrail Agent] --> (ALLOW) --> [Main Agent] --> [Tool Agent]
                             \--(BLOCK)--> [Reject Response]
    ```
    ''')
