from langchain.tools import tool_node
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode
from langchain.agents import create_agent
from react import llm,tools

SYSTEM_MESSAGE="""
You are a helpful assistant that can use tools to answer questions.
"""

def run_agent_reasoning(state:MessagesState) -> MessagesState:
    """
    Run the agent reasoning node.
    :param state:
    :return:
    """
    response=llm.invoke([{"role": "system", "content": SYSTEM_MESSAGE}, *state["messages"]])
    return {"messages": response}

tool_node=ToolNode(tools)