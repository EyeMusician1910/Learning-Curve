from langchain_core.output_parsers import StrOutputParser
from langsmith import Client
from langchain_ollama import ChatOllama

# 1. Initialize the client
client = Client()

# 2. Acknowledge the risk for this trusted prompt
prompt = client.pull_prompt("rlm/rag-prompt", dangerously_pull_public_prompt=True)

llm= ChatOllama(
    model="llama3.1",
    temperature=0
)
# 3. Your chain will now compile and bind perfectly
generation_chain = prompt | llm | StrOutputParser()