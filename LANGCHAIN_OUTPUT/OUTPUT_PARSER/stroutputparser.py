from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="huggingtweets/google",
    task="text-generation",
)

model= ChatHuggingFace(llm=llm)
response=model.invoke("What is the capital of India?")
print(response.content)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    input_variables=["topic"],
    template="Generate a detailed report on {topic}"
)

# 2nd prompt -> concise summary
template2 = PromptTemplate(
    input_variables=["text"],
    template="Generate a 5 line summary on the following text. /n {text}"
)

prompt1=template1.invoke("India")
response = model.invoke(prompt1)
# print(response.content)
prompt2=template2.invoke(response.content.replace("**", ""))
response = model.invoke(prompt2)
print(response.content.replace("**", ""))