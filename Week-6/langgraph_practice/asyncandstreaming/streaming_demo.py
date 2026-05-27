from typing import TypedDict
from langgraph.graph import END, START, StateGraph
from langgraph.types import StreamWriter

class HelloWorldState(TypedDict):
    message: str


def hello(state: HelloWorldState, writer: StreamWriter):
    writer({"custom_key" : "custom_values"})
    return {"message": "Hello "+state['message']}


def bye(state: HelloWorldState):
    return {"message": "Bye "+state['message']}


graph = StateGraph(HelloWorldState)
graph.add_node("hello",hello)
graph.add_node("bye",bye)

graph.add_edge(START,"hello")
graph.add_edge("hello","bye")
graph.add_edge("bye",END)

runnable = graph.compile()
# Streaming
for chunk in runnable.stream({"message":"Dharmik"},stream_mode="debug"):
    print(chunk)