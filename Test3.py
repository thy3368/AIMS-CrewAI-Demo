from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

############################用few-shot，给定一些例子，让模型学会某些特定的回复
examples = [
    {
        "question": "how are you?",
        "answer": "I'm fine, handsome man."
    },
    {
        "question": "What day of the week?",
        "answer": "It's Friday, handsome man."
    },
    {
        "question": "how is the weather?",
        "answer": "It's a sunny day, handsome man."
    },
]

example_prompt = PromptTemplate(template="Question:{question}\n{answer}",
                                input_variables=["question", "answer"])  # 设置一个提示模板

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question:{input}",  # 相当于一个后缀
    input_variables=["input"]
)

llm = ChatOpenAI(
    api_key="sk-XvWvy8rf8ewno0vVFmtgOMidGb5i3h1qNQmer7bE2buY6hlK",
    model_name="deepseek-chat",
    openai_api_base='https://tbnx.plus7.plus/v1',
    max_tokens=1024
)

response = llm.invoke(prompt.format(input="Why am I so ugly?"))

print("API Response:", response)
