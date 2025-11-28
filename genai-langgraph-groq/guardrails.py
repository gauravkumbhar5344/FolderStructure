from langchain_groq import ChatGroq

# -----------------------------
# Guardrail Prompt
# -----------------------------
GUARDRAIL_PROMPT = """
You are a guardrail model.
Your job is to ALLOW or BLOCK a user query.

Allowed domains:
- Banking queries
- Loan details, EMIs
- Technical questions (AI, ML, Python, SQL, coding)
- Career guidance
- General knowledge (non-sensitive)

NOT allowed:
- Personal identity
- Hate, abuse
- Political opinions
- Medical advice
- Illegal activities
- Hacking
- Fraud
- Sensitive personal info

Output ONLY:
ALLOW
or
BLOCK
"""

def ask(query: str, api_key: str):

    guardrail_llm = ChatGroq(
        api_key=api_key,
        model="groq/compound-mini"
    )

    main_llm = ChatGroq(
        api_key=api_key,
        model="llama-3.3-70b-versatile"
    )

    decision = guardrail_llm.invoke(
        GUARDRAIL_PROMPT + f"\n\nUser Query: {query}\n\nYour decision:"
    ).content.strip().upper()

    if "ALLOW" in decision:
        return main_llm.invoke(query).content

    return "❌ Your question is not allowed."
