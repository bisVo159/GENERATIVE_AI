from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.1)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    input_variables=["topic"],
    template="Generate a detailed report on {topic}"
)

# 2nd prompt -> concise summary
template2 = PromptTemplate(
    input_variables=["text"],
    template="Generate a 2 line summary on the following text. /n {text}"
)

# prompt1=template1.invoke("black holes in the universe")
# response = model.invoke(prompt1)
# print(response.content)
# prompt2=template2.invoke(response.content.replace("**", ""))
# response = model.invoke(prompt2)
# print("Concise Summary:")
# print(response.content.replace("**", ""))

# same code using chain
parser=str = StrOutputParser()
chain=template1 | model | parser | template2 | model | parser
response = chain.invoke("black holes in the universe")
print("Concise Summary using chain:")
print(response)