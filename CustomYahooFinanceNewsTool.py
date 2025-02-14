from langchain_community.tools import YahooFinanceNewsTool


class CustomYahooFinanceNewsTool(YahooFinanceNewsTool):
    def _run(self, query: str) -> str:
        try:
            import yfinance as yf
            company = yf.Ticker(query)
            news = company.news
            print(news)
            links = [n.get("link", n.get("url", "No link available")) for n in news]  # 尝试从多个字段中获取链接
            return "\n".join(links)
        except Exception as e:
            return f"Error: {e}"


tool = CustomYahooFinanceNewsTool()
response = tool.invoke("NVDA")
print(response)
