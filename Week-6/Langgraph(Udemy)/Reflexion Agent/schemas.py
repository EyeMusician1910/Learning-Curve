from typing import List

from pydantic import BaseModel, Field


class Reflection(BaseModel):
    missing: str = Field(description="Critique of what is missing.")
    superfluous : str = Field(description="Critique of what is superfluous.") #Unnecessary information

class AnswerQuestion(BaseModel):
    answer: str = Field(description="A detailed 250-words Answer of the question.")
    reflection: Reflection = Field(description="Your reflection on the initial answer.")
    search_queries : List[str] = Field(
        description="1-3 search queries for researching improvements to address the critique of your current answer."
    )

class ReviseAnswer(AnswerQuestion):
    """Revise the answer to the current question."""
    references :List[str] = Field(
        description="citations motivating your updated answer."
    )