from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent,AgentExecutor
from langchain_core.tools import tool
from langchain import hub
import requests

@tool
def get_weather_data(city: str) -> str:
  """
  This function fetches the current weather data for a given city
  """
  url = f'https://api.weatherstack.com/current?access_key=83955a7cce3decce7ceeda91a4b30e91&query={city}'

  response = requests.get(url)

  return response.json()

search_tool = DuckDuckGoSearchRun()
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash")

prompt = hub.pull("hwchase17/react")

agent=create_react_agent(
    llm=llm,
    tools=[search_tool,get_weather_data],
    prompt=prompt
)
agent_executor = AgentExecutor(
    agent=agent, 
    tools=[search_tool,get_weather_data], 
    verbose=True
)

def run_agent(query):
    response = agent_executor.invoke({"input": query})
    return response

if __name__ == "__main__":
    query = "todays weather in capital of west bengal"
    response = run_agent(query)
    print(response)
