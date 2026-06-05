from typing import Dict, Any
from graph.chains.generation import generation_chain
from graph.state import GraphState


def generate(state: GraphState) -> Dict[str, Any]:
    print("---Generate---")
    question = state["question"]
    documents = state["documents"]

    # Extract page_content from each document and join them into a single string
    docs_txt = "\n\n".join([doc.page_content for doc in documents])

    # Pass the plain text string as context
    generation = generation_chain.invoke({"context": docs_txt, "question": question})

    return {"documents": documents, "generation": generation, "question": question}