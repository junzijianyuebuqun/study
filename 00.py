import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# 设置智谱 GLM-4 的 API 地址和密钥
os.environ["OPENAI_API_KEY"] = "d112f1f6855f48f6baf1c3818d105171.qqZx9p6RIHSyJDJQ"
os.environ["OPENAI_API_BASE"] = "https://open.bigmodel.cn/api/paas/v4/"

# 使用 GLM-4 模型
model = ChatOpenAI(
    model="glm-4",
    temperature=0.7,
    timeout=30,
    max_tokens=1000,
    max_retries=6,
)

# 简单的单轮对话
response = model.invoke("为什么鹦鹉会说话？")
print(response.content)

# 多轮对话（带上下文记忆）
conversation = [
    SystemMessage("你是一个 helpful 的翻译助手，把英文翻译成中文。"),
    HumanMessage("翻译：I love programming."),
    AIMessage("我喜欢编程。"),
    HumanMessage("翻译：I love building applications.")
]

response = model.invoke(conversation)
print(response.content)

conversation = [
    {"role": "system", "content": "You are a helpful assistant that translates English to French."},
    {"role": "user", "content": "Translate: I love programming."},
    {"role": "assistant", "content": "J'adore la programmation."},
    {"role": "user", "content": "Translate: I love building applications."}
]

response = model.invoke(conversation)
print(response)  # AIMessage("J'adore créer des applications.")


from langchain.messages import HumanMessage, AIMessage, SystemMessage

conversation = [
    SystemMessage("You are a helpful assistant that translates English to French."),
    HumanMessage("Translate: I love programming."),
    AIMessage("J'adore la programmation."),
    HumanMessage("Translate: I love building applications.")
]

response = model.invoke(conversation)
print(response)  # AIMessage("J'adore créer des applications.")
print("输出结果正确")
print("6666")
print("master test")
print("hot-fix test")
print("111")
print("222-令狐冲")


