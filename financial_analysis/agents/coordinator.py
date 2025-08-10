import asyncio
from financial_analysis.agents.data_fetcher import DataFetcherAgent
from financial_analysis.agents.news_agent import NewsAgent
from financial_analysis.agents.expert_agent import FinancialExpertAgent

class CoordinatorAgent:
    def __init__(self, config):
        self.data_agent = DataFetcherAgent(config)
        self.news_agent = NewsAgent(config)
        self.expert_agent = FinancialExpertAgent(config)

    async def analyze(self, symbol, include_news=True, include_technical=True):
        stock_data = None
        news_data = None

        if include_technical:
            stock_data = await self.data_agent.fetch(symbol)

        if include_news:
            news_data = await self.news_agent.analyze(symbol)

        recommendation = self.expert_agent.generate(symbol, stock_data, news_data)

        return {
            "symbol": symbol,
            "stock_data": stock_data,
            "news_data": news_data,
            "recommendation": recommendation
        }
