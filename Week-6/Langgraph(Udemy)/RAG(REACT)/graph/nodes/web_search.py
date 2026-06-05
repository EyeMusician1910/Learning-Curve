from typing import Dict,Any
from langchain_core.documents import Document
from langchain_community.tools import DuckDuckGoSearchResults # ◄ Switched to results wrapper


from graph.state import GraphState

web_search_tool = DuckDuckGoSearchResults(max_results=3,output_format="list")

def web_search(state: GraphState)-> Dict[str, Any]:
    print("---Web Search---")
    question = state["question"]
    documents = state.get("documents",[])
    results=web_search_tool.invoke({"query" : question})
    joined_ddg_result = "\n".join(
        [res["snippet"] for res in results]
    )
    web_results= Document(page_content=joined_ddg_result)
    if documents is not None:
        documents.append(web_results)
    else:
        documents = [web_results]
    return {"documents":documents , "question":question}
if __name__ == "__main__":
    web_search(state={"question" : "agent memory", "documents" : None})#Scenario if no document was found relevant