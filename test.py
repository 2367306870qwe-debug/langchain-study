import os
# 正确导入DeepSeek
from langchain_deepseek import ChatDeepSeek

os.environ["DEEPSEEK_API_KEY"] = 'sk-2831e0e162d24451b7a8b63bd3d02821'

# 初始化对话模型
llm = ChatDeepSeek(
    model="deepseek-chat",
    max_tokens=1024
)
# invoke 标准调用方式，不能直接 llm(字符串)
res = llm.invoke("介绍codex")
print(res.content)