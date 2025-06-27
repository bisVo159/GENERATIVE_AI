from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests

@tool
def multiply(a: int, b: int) -> int:
  """Given 2 numbers a and b this tool returns their product"""
  return a * b

print(multiply.invoke({'a':3, 'b':4}))

# tool binding
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash")
llm_with_tools = llm.bind_tools([multiply])
print(llm_with_tools.invoke("can you add 2 with 3"))

query = HumanMessage('can you multiply 3 with 1000')
messages = [query]

result = llm_with_tools.invoke(messages)
messages.append(result)
print(messages)

# llm does not execute tools
print(result.tool_calls[0])
tool_result = multiply.invoke(result.tool_calls[0])
print(tool_result)
messages.append(tool_result)

print(llm_with_tools.invoke(messages).content)