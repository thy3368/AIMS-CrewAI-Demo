from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

# 定义一个模板，用于生成问题的回答
template = """根据以下信息回答问题：
{context}
问题：{question}
回答："""

# 创建一个提示模板
prompt = PromptTemplate(template=template, input_variables=["context", "question"])

# 创建一个 LLMChain，使用 OpenAI 作为模型

llm = ChatOpenAI(
    api_key="sk-XvWvy8rf8ewno0vVFmtgOMidGb5i3h1qNQmer7bE2buY6hlK",
    model_name="deepseek-chat",
    openai_api_base='https://tbnx.plus7.plus/v1',
    max_tokens=1024
)

chain = LLMChain(llm=llm, prompt=prompt)

# 使用链来回答问题
context = "DeepSeek是一种深度学习框架，主要用于大规模的机器学习任务。"
question = "什么是DeepSeek？"
response = chain.run(context=context, question=question)
print(response)
