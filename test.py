from dotenv import load_dotenv
load_dotenv()  

from langchain.chat_models import init_chat_model
import os
base_url = os.getenv("DASHSCOPE_BASE_URL")
api_key = os.getenv("DASHSCOPE_API_KEY")
model = init_chat_model(
    model="qwen3-omni-flash",
    model_provider="openai",
    base_url=base_url,
    api_key=api_key
)

print(model.invoke("告诉我你现在使用的模型的完整名称"))




