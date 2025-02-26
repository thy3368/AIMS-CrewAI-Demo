# pip3 install langchain_openai
# python3 deepseek_v2_langchain.py
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key="sk-XvWvy8rf8ewno0vVFmtgOMidGb5i3h1qNQmer7bE2buY6hlK",
    model_name="deepseek-chat",
    openai_api_base='https://tbnx.plus7.plus/v1',
    max_tokens=1024
)

response = llm.invoke("给我一个很土但是听起来很好养活的男孩小名", temperature=1)

print("API Response:", response)

# if isinstance(response, str):
#     print("API Response:", response)
# else:
#     print(response.content)


response = llm.invoke("Hi!")
print(response.content)

text = "做logo的公司的好名字是什么？"
message = [HumanMessage(content=text)]

response1 = llm.invoke(message)
print(response1.content)
