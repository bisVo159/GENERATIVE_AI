from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-exp-03-07",dimensions=5)
result = embeddings.embed_query("Delhi is the capital of India")
print(len(result))