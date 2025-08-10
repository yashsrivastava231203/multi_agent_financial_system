import asyncio
import sys
from financial_analysis.config import get_config
from financial_analysis.agents.coordinator import CoordinatorAgent

async def run_analysis(symbol, include_news=True, include_technical=True):
    config = get_config()
    agent = CoordinatorAgent(config)
    result = await agent.analyze(symbol, include_news, include_technical)

    print("\n=== Analysis Report ===")
    print(f"Symbol: {result['symbol']}")
    print(f"\n📈 Stock Data:\n{result['stock_data']}")
    print(f"\n📰 News Analysis:\n{result['news_data']}")
    print(f"\n💡 Recommendation:\n{result['recommendation']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python financial_analysis.py SYMBOL")
    else:
        symbol = sys.argv[1]
        asyncio.run(run_analysis(symbol))
