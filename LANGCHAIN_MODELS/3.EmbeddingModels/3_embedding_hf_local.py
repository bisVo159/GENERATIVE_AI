from langchain_huggingface import HuggingFaceEmbeddings
import os

target_dir = "D:/hf_models/emb"
os.environ["HF_HOME"] = target_dir

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

vector = embedding.embed_documents(documents)

print("Embedding shape:", len(vector), "x", len(vector[0]))