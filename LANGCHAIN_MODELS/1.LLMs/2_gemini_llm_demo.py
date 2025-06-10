from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAI

# Load your .env file
load_dotenv()
# api_key = os.getenv("GOOGLE_API_KEY")

model = GoogleGenerativeAI(model="gemini-1.5-flash-latest")
prompt="What is the capital of India?"

response = model.invoke(prompt)
print(response.replace('**', ''))
