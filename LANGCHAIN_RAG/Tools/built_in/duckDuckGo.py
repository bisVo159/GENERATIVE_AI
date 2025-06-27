from langchain_community.tools import DuckDuckGoSearchRun,DuckDuckGoSearchResults

search_tool = DuckDuckGoSearchRun()
results1= search_tool.invoke("top news in india today")

print(search_tool.name)
print(search_tool.description)
print(search_tool.args)

print(results1)

search = DuckDuckGoSearchResults(output_format="list")
results2= search.invoke("top news in india today")

print("Results in list format:")

print(type(results2))