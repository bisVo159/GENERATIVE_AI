from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.1)

template = PromptTemplate(
    input_variables=["topic"],
    template="Generate 5 interesting facts about {topic}"
)

parser=str = StrOutputParser()

chain = template | model | parser
response = chain.invoke("black holes in the universe")

print("Interesting Facts:")
print(response)

chain.get_graph().print_ascii()
