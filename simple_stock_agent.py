from crewai import Agent, Task
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from langchain_openai import ChatOpenAI


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
            tools=[YahooFinanceNewsTool()],
            allow_delegation=False
        )

    def create_analysis_task(self, company):
        return Task(
            description=f"""
            分析 {company} 的股票情况，包括：
            1. 最近的新闻动态
            2. 市场表现
            3. 投资建议
            请提供详细的分析报告。
            """,
            expected_output="A comprehensive stock analysis report including recent news, market performance, and investment recommendations.",
            agent=self.analyst
        )


if __name__ == "__main__":
    agent_creator = SimpleStockAgent()
    analyst = agent_creator.create_analyst()
