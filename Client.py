from langchain import LLMMathChain
from langchain.agents import AgentType
from langchain.agents import initialize_agent, Tool
from openai import OpenAI

llm = OpenAI(api_key="sk-XvWvy8rf8ewno0vVFmtgOMidGb5i3h1qNQmer7bE2buY6hlK",
             base_url="https://tbnx.plus7.plus/v1")


# 简单定义函数作为一个工具
def personal_info(name: str):
    info_list = {
        "Artorias": {
            "name": "Artorias",
            "age": 18,
            "sex": "Male",
        },
        "Furina": {
            "name": "Furina",
            "age": 16,
            "sex": "Female",
        },
    }
    print(info_list)
    if name not in info_list:
        return None
    return info_list[name]


# 自定义工具字典
tools = (
    # 这个就是上面的llm-math工具
    Tool(
        name="Calculator",
        description="Useful for when you need to answer questions about math.",
        func=LLMMathChain.from_llm(llm=llm).run,
        coroutine=LLMMathChain.from_llm(llm=llm).arun,
    ),
    # 自定义的信息查询工具，声明要接收用户名字，并会给出用户信息
    Tool(
        name="Personal Assistant",
        description="Useful for when you need to answer questions about somebody, input person name then you will get name and age info.",
        func=personal_info,
    )
)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# 提问，询问Furina用户的年龄的0.43次方
rs = agent.run("What's the person Furina's age raised to the 0.43 power?")
print(rs)
