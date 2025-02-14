from crewai import Agent, Task
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from langchain_openai import ChatOpenAI
from tools.database_tools import DatabaseTools


class SimpleStockAgent:
    def __init__(self):
        self.llm = ChatOpenAI(
            api_key="sk-XvWvy8rf8ewno0vVFmtgOMidGb5i3h1qNQmer7bE2buY6hlK",
            model_name="deepseek-chat",
            openai_api_base='https://tbnx.plus7.plus/v1',
            max_tokens=1024
        )
        self.analyst = self.create_analyst()

    def create_analyst(self):
        return Agent(
            role="Stock Market Analyst",
            goal="Analyze stocks and provide investment insights",
            backstory="An experienced stock analyst with expertise in market analysis",
            verbose=True,
            llm=self.llm,
            tools=[
                YahooFinanceNewsTool(),
                DatabaseTools.query_stock,
                DatabaseTools.insert_stock
            ],
            allow_delegation=False
        )

    def create_analysis_task(self, company):
        return Task(
            description=f"""
            分析 {company} 的股票情况。

            请按照以下步骤进行分析：
            1. 获取最近的新闻动态
               - 使用 yahoo_finance_news 工具
               - 直接输入: AAPL（不要使用任何JSON或字典格式）
            
            2. 分析市场表现
               - 基于新闻内容分析市场表现
               - 关注重要指标和趋势
            
            3. 提供投资建议
               - 基于以上分析给出具体建议
            
            输出要求：
            - 提供完整的分析报告
            - 确保内容清晰、专业
            - 给出具体的投资建议
            """,
            expected_output="A comprehensive stock analysis report including recent news, market performance, and investment recommendations.",
            agent=self.analyst
        )


if __name__ == "__main__":
    agent_creator = SimpleStockAgent()
    analyst = agent_creator.create_analyst()
