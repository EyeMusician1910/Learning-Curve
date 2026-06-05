from dotenv import load_dotenv


load_dotenv()

from pprint import pprint
from graph.chains.generation import generation_chain
from graph.chains.retrieval_grader import  GradeDocuments, retrieval_grader
from ingestion import retriever
from graph.chains.hallucination_grader import hallucination_grader, GradeHallucinations
from graph.chains.router import question_router, RouteQuery


def test_retrieval_grader_answer_yes()->None:
    question = "agent memory"
    docs = retriever.invoke(question)
    doc_txt = docs[0].page_content
    res : GradeDocuments = retrieval_grader.invoke(
        {
            "question": question,"document": doc_txt
        }
    )

    assert res.binary_score == "yes"
def test_retrieval_grader_answer_no()->None:
    question = "agent memory"
    docs = retriever.invoke(question)
    doc_txt = docs[0].page_content
    res : GradeDocuments = retrieval_grader.invoke(
        {
            "question": "how to make pizza","document" : doc_txt
        }
    )

    assert res.binary_score == "no"

def test_generation_chain() -> None:
    quesion = "agent memory"
    docs =retriever.invoke(quesion)
    generation= generation_chain.invoke({"context":docs , "question":quesion})
    pprint(generation)

def test_hallucination_grader_ans_yes() -> None:
    question = "agent memory"
    docs=retriever.invoke(question)
    generation= generation_chain.invoke({"context": docs,"question": question})
    res: GradeHallucinations = hallucination_grader.invoke(
        {
            "documents": docs,
            "generation": generation
        }
    )
    assert res.binary_score

def test_hallucination_grader_ans_no() -> None:
    question = "agent memory"
    docs=retriever.invoke(question)
    res: GradeHallucinations = hallucination_grader.invoke(
        {
            "documents": docs,
            "generation": "In order to make pizza,we'll need to first make the dough."
        }
    )
    assert res.binary_score

def test_router_to_vectorstore() -> None:
    quesion = "agent memory"
    res: RouteQuery = question_router.invoke({"question": quesion})
    assert res.datasource=="vectorstore"

def test_router_to_websearch() -> None:
    quesion = "how to make pizza?"
    res: RouteQuery = question_router.invoke({"question": quesion})
    assert res.datasource=="websearch"