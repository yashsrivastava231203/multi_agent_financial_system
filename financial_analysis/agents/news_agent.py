import aiohttp
import openai

class NewsAgent:
    def __init__(self, config):
        self.news_api_key = config["NEWS_API_KEY"]
        self.openai_api_key = config["OPENAI_API_KEY"]
        openai.api_key = self.openai_api_key

    async def analyze(self, symbol):
        url = f"https://newsapi.org/v2/everything?q={symbol}&sortBy=publishedAt&apiKey={self.news_api_key}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return {"sentiment": "unknown", "confidence": 0, "error": "News API error"}
                data = await resp.json()
                headlines = [article["title"] for article in data.get("articles", [])][:5]
                if not headlines:
                    return {"sentiment": "neutral", "confidence": 50, "error": "No news available"}

                prompt = f"Analyze the sentiment of these news headlines about {symbol}: {headlines}"
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                reply = response["choices"][0]["message"]["content"]
                return {
                    "sentiment": "positive" if "positive" in reply.lower() else "negative" if "negative" in reply.lower() else "neutral",
                    "confidence": 70,
                    "summary": reply
                }
