import datetime
from dotenv import load_dotenv
from pydantic.v1.json import isoformat

from schemas import AnswerQuestion, ReviseAnswer

load_dotenv()

from langchain_core.output_parsers.openai_tools import (
    JsonOutputToolsParser,
    PydanticToolsParser
) #Takes back the response we get the llm with the function calling invocation # and it'll take the function calling invocation to either transform it into JSON,to a dictionary or into a pydantic obj.

from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama

llm= ChatOllama(
    model = "llama3.1",
    temperature = 0.1,
)

parser = JsonOutputToolsParser(return_id=True)
parser_pydantic = PydanticToolsParser(tools=[AnswerQuestion])
def get_current_time(*args, **kwargs) -> str:
    return datetime.datetime.now().isoformat()


actor_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are expert researcher.
            Current time: {time}
            
            1. {first_instruction}
            2. Reflect and critique your answer. Be severe to maximize improvement.
            3. Recommend search queries to research information and improve your answer.""",
        ),
        MessagesPlaceholder(variable_name="messages"), #technique to reuse the conversation,saves the information of the conversation
        ("system", "Answer the user's question above using the required format."),
    ]
).partial( #use this to populate some already known placeholders
    time=get_current_time
)

first_responder_prompt_template = actor_prompt_template.partial(
    first_instruction= "Provide a detailed ~250 word answer."
)

first_responder =  first_responder_prompt_template.partial() | llm.bind_tools(
    tools=[AnswerQuestion], tool_choice="AnswerQuestion"
)
#a set of instructions to create the revised answers
revise_instructions = """Revise your previous answer using the new information.
    - You should use the previous critique to add important information to your answer.
        - You MUST include numerical citations in your revised answer to ensure it can be verified.
        - Add a "References" section to the bottom of your answer (which does not count towards the word limit). In form of:
            - [1] https://example.com
            - [2] https://example.com
    - You should use the previous critique to remove superfluous information from your answer and make SURE it is not more than 250 words.
"""

revisor= actor_prompt_template.partial(
    first_instruction= revise_instructions
) | llm.bind_tools(tools=[ReviseAnswer], tool_choice="ReviseAnswer")

if __name__ == "__main__":
    human_message =HumanMessage(
        content="Write about AI-Powered SOC / autonomous soc  problem domain,"
                " list startups that do that and raised capital."
    )
    chain = (
            first_responder_prompt_template
            | llm.bind_tools(tools=[AnswerQuestion], tool_choice="AnswerQuestion")
            | parser_pydantic
    )
    res = chain.invoke(input={"messages": [human_message]})
    print(res)