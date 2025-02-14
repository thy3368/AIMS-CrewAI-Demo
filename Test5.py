from langchain.chains.conversation.base import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    api_key="sk-XvWvy8rf8ewno0vVFmtgOMidGb5i3h1qNQmer7bE2buY6hlK",
    model_name="deepseek-chat",
    openai_api_base='https://tbnx.plus7.plus/v1',
    max_tokens=1024
)

# 初始化对话链
conversation = ConversationChain(llm=llm, memory=ConversationBufferMemory())

conversation.invoke("今天早上猪八戒吃了2个人参果。")
print("记忆1: ", conversation.memory.buffer)
print()

conversation.invoke("下午猪八戒吃了1个人参果。")
print("记忆2: ", conversation.memory.buffer)
print()

conversation.invoke("晚上猪八戒吃了3个人参果。")
print("记忆3: ", conversation.memory.buffer)
print()

conversation.invoke("猪八戒今天一共吃了几个人参果？")
print("记忆4提示: ", conversation.prompt.template)
print("记忆4: ", conversation.memory.buffer)
