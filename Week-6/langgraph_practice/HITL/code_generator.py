from typing import List, TypedDict,TypedDict
from langgraph.graph import StateGraph,START,END
from langgraph.checkpoint.memory import MemorySaver
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langgraph.types import interrupt, Command

llm = ChatOllama(
    model="llama3.1",
    temperature=0
)

class CodingAssitantState(TypedDict):
    task: str
    code: str
    tests: str
    
code_prompt= ChatPromptTemplate.from_template("Generate Python code for : {task}")
test_prompt= ChatPromptTemplate.from_template("Write unit tests for this code: /n {code}")

code_chain= code_prompt | llm | StrOutputParser()
test_chain= test_prompt | llm | StrOutputParser()

def generate_code(state):
    print("Generating code...")
    code = code_chain.invoke({"task" : state["task"]})
    return Command(goto="human_review" , update={"code":code})

def human_review(state):
    value=interrupt({})
    if value == "Yes":
        return Command(goto="create_tests")
    else:
        return Command(goto=END)

def create_tests(state):
    tests=test_chain.invoke({"code": state["code"]})
    return Command(goto=END, update = {"tests":tests})

def create_coding_assitant_workflow():
    workflow= StateGraph(CodingAssitantState)
    workflow.add_node("generate_code", generate_code)
    workflow.add_node("human_review", human_review)
    workflow.add_node("create_tests", create_tests)
    workflow.set_entry_point("generate_code")
    return workflow.compile(checkpointer=MemorySaver())

coding_assistant= create_coding_assitant_workflow()
inputs={"task" : "Create a function to reverse a string in Python"}
thread= {"configurable": {"thread_id" : 1}}
result= coding_assistant.invoke(inputs, config=thread)

print("--- Generated Code---")
print(result["code"])

user_input= input("Are you OK with the code? Type Yes or No.")
result=coding_assistant.invoke(Command(resume=user_input), config=thread)

print("\n--- Generated Tests ---")
print(result.get("tests","No code or tests generated"))