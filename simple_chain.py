from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt=PromptTemplate(
    template="What is a good name for a company that makes {product}?",
    input_variables=["product"]
)

model=ChatOpenAI()
parser=StrOutputParser()
chain= prompt | model | parser
print(chain.invoke({"product": "colorful socks"}))

chain.get_graph().print_ascii()  # to visualize the chain