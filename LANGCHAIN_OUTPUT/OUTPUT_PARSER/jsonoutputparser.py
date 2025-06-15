from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.1)

parser=str = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain=template | model | parser
print(parser.get_format_instructions())
response = chain.invoke({'topic':'black hole'})
print(type(response))
print(len(response))
print(response)

# but using  jsonoutputparser we cant define schema