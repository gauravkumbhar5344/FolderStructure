import math

def run_tool(tool_name: str, tool_input: str):
    tool_name = tool_name.lower()
    if tool_name == 'calculator':
        return safe_calc(tool_input)
    elif tool_name == 'web search (mock)':
        return mock_search(tool_input)
    else:
        return 'Unknown tool'

def safe_calc(expr: str):
    # Very small safe evaluator for arithmetic expressions (no names, no imports)
    allowed_chars = '0123456789+-*/(). %'
    if any(c not in allowed_chars for c in expr):
        return 'Invalid characters in expression.'
    try:
        # eval with restricted globals and locals
        result = eval(expr, {'__builtins__': None}, {})
        return f'Result: {result}'
    except Exception as e:
        return f'Calculation error: {e}'

def mock_search(query: str):
    return f"(mock) Top results for '{query}':\n- Result A - summary\n- Result B - summary"
