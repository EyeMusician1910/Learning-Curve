from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults


@tool
def triple(num:float)-> float:
    """param num: a number to triple it
    returns: the triple of the input number"""

    return num*3
tools = [
    DuckDuckGoSearchResults(max_results=1, output_format="string"),
    triple
]

llm=ChatOllama(
    model="llama3.1",
    temperature=0.1,
).bind_tools(tools)