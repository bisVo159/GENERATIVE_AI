from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.1)

parser1=StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive','negetive','neutral'] = Field(description="Give the sentiment of the feedback")

parser2=PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback}\n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={
        "format_instruction": parser2.get_format_instructions()
    }
)

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback in two line \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback in two line \n {feedback}',
    input_variables=['feedback']
)

classifier_chain = prompt1 | model | parser2

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive',prompt2 | model | parser1) ,
    (lambda x: x.sentiment == 'negetive',prompt3 | model | parser1) ,
    RunnableLambda(lambda x: "No response needed")
)

chain = classifier_chain | branch_chain

# print(chain.invoke({'feedback': 'This is a beautiful phone'}))

# print(chain.invoke({'feedback': 'This is a bad phone'}))
print(chain.invoke({'feedback': 'This is a phone'}))
# print(chain.invoke({'feedback': 'This is a phone with no issues'}))
# print(chain.invoke({'feedback': 'This is a phone with no issues but I am not happy with the service'}))
# print(chain.invoke({'feedback': 'This is a phone with no issues but I am not happy with the service. The delivery was late.'}))

chain.get_graph().print_ascii()