# Document loaders are components in LC used to load data from various sources into a standardized format(usually as document objects), which can then be used for chunking, embedding. retrieval and generation
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.1)

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

loader=TextLoader('cricket.txt', encoding='utf-8')
docs=loader.load()
print(type(docs))
print(docs[0].page_content)

chain=prompt | model | parser
print("Summary of the poem: ")
print(chain.invoke({'poem': docs[0].page_content}))