from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema,StructuredOutputParser

load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.1)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser=str = StructuredOutputParser.from_response_schemas(schema)

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