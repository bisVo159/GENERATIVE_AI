from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv  

load_dotenv()
chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperature=0.5)
prompt1 = "suggest me 5 indian male names"
prompt2 = "write 5 line poem on cricket"
response = chat_model.invoke(prompt2)       
print(response.content.replace('**', ''))  