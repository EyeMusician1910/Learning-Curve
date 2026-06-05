from dotenv import load_dotenv
load_dotenv()

from langchain_tavily import TavilySearch
from langchain_core.tools import StructuredTool #allow us to convert pyton functions into a tool that can be used by LLMs.
from langgraph.prebuilt import ToolNode #checks the last message and checks if there are any tool calls needed.
from schemas import AnswerQuestion,ReviseAnswer

tavily_tool= TavilySearch(max_results=5)

def run_queries(search_queries : list[str], **kwargs ):
    """Run the genereated queries."""
    return tavily_tool.batch([{"query": query} for query in search_queries])

execute_tools = ToolNode(
    [
        StructuredTool.from_function(run_queries, name=AnswerQuestion.__name__),
        StructuredTool.from_function(run_queries, name=ReviseAnswer.__name__),
    ]
)