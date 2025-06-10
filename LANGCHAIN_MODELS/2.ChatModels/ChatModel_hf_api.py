from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm=HuggingFaceEndpoint(
        repo_id="sarvamai/sarvam-m", 
        # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", 
        task="text-generation",
        pipeline_kwargs=dict(
            temparature=0.5,
            max_new_tokens= 10
            )
    )

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of India?")
print(result.content)  
# print(result.content.split('\n')[-1]) 
