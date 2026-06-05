import operator
from typing import TypedDict,Annotated,Any
from urllib.response import addinfo

from langgraph.graph import START,END,StateGraph

class State(TypedDict):
    aggregate:Annotated[list, operator.add]
class ReturnNodeValue:
    def __init__(self,node_secret : str):
        self._value=node_secret
    def __call__(self,state:State) -> Any:
        import time
        time.sleep(3)
        print(f"Adding {self._value} to {state['aggregate']}")
        return {"aggregate":[self._value]}

builder= StateGraph(State)
builder.add_node("A",ReturnNodeValue("I'm A"))
builder.add_edge(START,"A")
builder.add_node("B",ReturnNodeValue("I'm B"))
builder.add_node("C",ReturnNodeValue("I'm C"))
builder.add_node("D",ReturnNodeValue("I'm D"))
builder.add_node("B2",ReturnNodeValue("I'm B2"))
builder.add_edge("A","B")
builder.add_edge("A","C")
builder.add_edge("B","B2")
builder.add_edge(["B2","C"],"D") #Convenient way to make multiple edges in one line
builder.add_edge("D",END)

graph=builder.compile()
graph.get_graph().draw_mermaid_png(output_file_path="async.png")

if __name__ == "__main__":
    print("Hello Async!!")
    graph.invoke({"aggregate" : []}, {"configurable" : {"thread_id" : "foo"}})