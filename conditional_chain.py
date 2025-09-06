from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model=ChatOpenAI()

parser=StrOutputParser()

class FeedbackSentiment(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(..., description="The sentiment of the feedback")

parser2=PydanticOutputParser(pydantic_object=FeedbackSentiment)

prompt1=PromptTemplate( 
    template="classify the sentiment of the following feedback text into positive and negative \n {feedback}\n {format_instructions}",
    input_variables=["feedback"],partial_variables={"format_instructions": parser2.get_format_instructions()}
)

classifier_chain= prompt1 | model | parser2

prompt2=PromptTemplate(
    template="write a appopriate response to this positive feedbackk: {feedback}",
    input_variables=["feedback"]
)
prompt3=PromptTemplate(
    template="write a appopriate response to this negative feedback: {feedback}",   
    input_variables=["feedback"]
)

branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='positive', prompt2 | model | parser),
    (lambda x:x.sentiment=='negative', prompt3 | model | parser),
    RunnableLambda( lambda x: "couldn't classify the feedback" )
)

final_chain= classifier_chain | branch_chain

print(final_chain.invoke({"feedback": "The product quality is excellent and delivery was prompt!"}))
final_chain.get_graph().print_ascii()  # to visualize the chain