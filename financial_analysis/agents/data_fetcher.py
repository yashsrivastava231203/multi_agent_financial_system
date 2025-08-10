import aiohttp
import asyncio

class DataFetcherAgent:
    def __init__(self, config):
        self.api_key = config["POLYGON_API_KEY"]
        self.base_url = "https://api.polygon.io/v2/aggs/ticker"

    async def fetch(self, symbol):
        url = f"{self.base_url}/{symbol}/prev?adjusted=true&apiKey={self.api_key}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return {"error": f"Polygon API error: {resp.status}"}
                data = await resp.json()
                result = data["results"][0]
                return {
                    "symbol": symbol,
                    "current_price": result["c"],
                    "previous_close": result["c"],
                    "volume": result["v"]
                }
