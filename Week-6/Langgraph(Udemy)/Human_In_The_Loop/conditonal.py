import operator
from typing import TypedDict, Annotated, Any, Sequence
from urllib.response import addinfo

from langgraph.checkpoint.sqlite import build_delta_stage2_sql
from langgraph.graph import START,END,StateGraph

class State(TypedDict):
    aggregate:Annotated[list, operator.add]
    which:str #holds which node we want to execute
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
builder.add_node("E",ReturnNodeValue("I'm E"))

def route_bc_or_cd(state:State) -> Sequence[str]:
    if state["which"] == "CD":
        return ["C", "D"]
    return ["B","C"]

intermediates= ["B","C","D"]
builder.add_conditional_edges(
    "A",
    route_bc_or_cd,
    intermediates,
)
for node in intermediates:
    builder.add_edge(node,"E")
builder.add_edge("E",END)
graph=builder.compile()
graph.get_graph().draw_mermaid_png(output_file_path="conditonal.png")

if __name__ == "__main__":
    print("Hello Async!!")
    graph.invoke({"aggregate" : [], "which" : ""}, {"configurable" : {"thread_id" : "foo"}})