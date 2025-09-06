from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1=ChatOpenAI(model_name="gpt-3.5-turbo")
model2=ChatOpenAI(model_name="gpt-4")

prompt1=PromptTemplate( 
    template="generate short and simple notes from the given text \n {text}",
    input_variables=["text"]    
)

prompt2=PromptTemplate(
    template="generate 5 short question answer from the following text \n {text}",
    input_variables=["text"]
)

prompt3=PromptTemplate(
    template="merge the provided notes and quiz into a single document \n notes: {notes} \n quiz: {quiz}",
    input_variables=["notes", "quiz"]
)

parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain= parallel_chain | prompt3 | model1 | parser
print(merge_chain.invoke({"text": "LangChain is a framework for developing applications powered by language models. It can be used for chatbots, Generative Question-Answering (GQA), summarization, and much more. It is designed to be modular and flexible, allowing developers to easily integrate different components and customize their applications."}))
merge_chain.get_graph().print_ascii()  # to visualize the chain
