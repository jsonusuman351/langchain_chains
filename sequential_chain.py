from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1=PromptTemplate(
    template="detail report about company that makes {product}?",
    input_variables=["product"]
)
prompt2=PromptTemplate(
    template="give me five line summary of this report: {report}",  
    input_variables=["report"]
)

model=ChatOpenAI()
parser=StrOutputParser()
chain= prompt1 | model | parser | prompt2 | model | parser
print(chain.invoke({"product": "colorful socks"}))  
chain.get_graph().print_ascii()  # to visualize the chain