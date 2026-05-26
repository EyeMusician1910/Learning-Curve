import asyncio
import langchain_core
import langchain_community
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# The absolute newest 2026 agent import (replacing create_react_agent)
from langchain.agents import create_agent

# Real tool imports
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_experimental.tools import PythonREPLTool

llm = ChatOllama(
    model="llama3.1",
    temperature=0.5
)


# making some cool pet names for our pet


def generate_pet_name(animal_type, pet_color):
    
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that suggests cool names for pets."),
        ("human", "I have a pet {animal_type} and I want a cool name for it. It's color is {pet_color}.Suggest me five cool names for my pet.")
    ])
    
    name = prompt_template | llm | StrOutputParser()
    response = name.invoke({"animal_type": animal_type, "pet_color": pet_color})
    return response


def langchain_agents():
    llm = ChatOllama(
        model="llama3.1",
        temperature=0
    )
    
    # 1. Setup actual working tool instances
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    math_tool = PythonREPLTool()
    tools = [wikipedia, math_tool]
    
    # 2. Modern v1.0 Agent factory (Cleaner, accepts a system prompt parameter directly)
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt="You are a helpful assistant that can search Wikipedia and run math calculations."
    )
    
    # 3. Running the agent 
    result = agent.invoke({"messages": [("human", "What is the average age of a dog? multiply it by 3.")]})
    print(result["messages"][-1].content)


if __name__ == "__main__":
    langchain_agents()
    # print(generate_pet_name("cat","black and white"))