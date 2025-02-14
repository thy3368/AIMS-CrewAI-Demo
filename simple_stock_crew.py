from crewai import Crew

from simple_stock_agent import SimpleStockAgent


class SimpleStockCrew:
    def __init__(self, company):
        self.company = company
        self.stock_agent = SimpleStockAgent()

    def run(self):
        analysis_task = self.stock_agent.create_analysis_task(self.company)

        crew = Crew(
            agents=[self.stock_agent.analyst],
            tasks=[analysis_task]
        )

        result = crew.kickoff()
        return result


if __name__ == "__main__":
    company = "Apple"
    stock_crew = SimpleStockCrew(company)
    result = stock_crew.run()
    print(result)
