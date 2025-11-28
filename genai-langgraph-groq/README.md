# GenAI LangGraph + Groq Streamlit Demo

Small demo project that shows:
- Streamlit frontend with authentication
- Sidebar to input Groq API key and select a tool
- Guardrail-based check (uses langchain_groq.ChatGroq in code)
- A simple Calculator tool (safe eval) and a mock WebSearch tool
- Mock LangGraph connector to visualize multi-agent layout (no external LangGraph dependency required)

## Run
1. Create a virtual environment
2. `pip install -r requirements.txt`
3. Set your GROQ_API_KEY in the sidebar (or use env/test)
4. `streamlit run streamlit_app.py`

Notes:
- This demo assumes `langchain_groq` is available. If you don't have access to Groq, the app still works: guardrail/main LLM calls will error unless you provide a valid API key.
- The LangGraph connector here is mocked to avoid extra dependencies; replace with real LangGraph flows if desired.
