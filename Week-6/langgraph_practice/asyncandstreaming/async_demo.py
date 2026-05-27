from pydantic import BaseModel,Field
from langgraph.graph import END, START, StateGraph
from util.langgraph_util import display
import asyncio
class HelloWorldState(BaseModel):
    message: str = Field(min_length=3,max_length=100)


async def hello(state: HelloWorldState):
    print(f"Hello Node: {state.message}")
    #To simulate the async function
    await asyncio.sleep(1)
    return {"message": "Hello "+state.message}


async def bye(state: HelloWorldState):
    print(f"Bye Node: {state.message}")
    #To simulate the async function
    await asyncio.sleep(1)
    return {"message": "Bye "+state.message}


graph = StateGraph(HelloWorldState)
graph.add_node("hello",hello)
graph.add_node("bye",bye)

graph.add_edge(START,"hello")
graph.add_edge("hello","bye")
graph.add_edge("bye",END)

runnable = graph.compile()
#async invocation
async def main():
    output = await runnable.ainvoke({"message": "Dharmik"})
    print(output)
    
asyncio.run(main())