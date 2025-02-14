from openai import OpenAI

client = OpenAI(api_key="sk-XvWvy8rf8ewno0vVFmtgOMidGb5i3h1qNQmer7bE2buY6hlK",
                base_url="https://tbnx.plus7.plus/v1")

tools = [{
    "type": "function",
    "function": {
        "name": "calculator",
        "description": "运行加减乘除运算的表达式。",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "需要运行的算术表达式"
                }
            }
        }
    }
}]

messages = [{"role": "user", "content": "计算 100*100/400*56 的值？"}]

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
    tools=tools
)

print(response)
