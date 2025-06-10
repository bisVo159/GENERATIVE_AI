from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
import os

load_dotenv()

target_dir = "D:/hf_models/TinyLlama"
os.environ["HF_HOME"] = target_dir
llm=HuggingFacePipeline.from_model_id(
        model_id="sarvamai/sarvam-m", 
        # model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", 
        task="text-generation",
        pipeline_kwargs=dict(
            temparature=0.5,
            max_new_tokens= 10
            )
    )

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of India?")
print(result.content)  