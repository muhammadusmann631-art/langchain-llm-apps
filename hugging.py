from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
# "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

load_dotenv()
HUGGING_FACE_KEY = os.getenv("HUGGING_API_KEY")

if not HUGGING_FACE_KEY:
    raise ValueError("APi key shai dalo ")

llm=HuggingFaceEndpoint(
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    temperature=0.4,
    max_new_tokens=20,
    huggingfacehub_api_token=HUGGING_FACE_KEY
)

model =ChatHuggingFace(llm = llm)
result =  model.invoke("How are you today")
print("result output\n", result)