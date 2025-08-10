import httpx
import json

class FinancialExpertAgent:
    def __init__(self, config):
        self.api_key = config["OPENAI_API_KEY"]
        self.model = "mixtral-8x7b-32768"  # or "llama3-70b-8192"

    def generate(self, symbol, stock_data, news_data):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        prompt = f"""
You are a financial expert AI. Analyze this stock:

Symbol: {symbol}
Stock Data: {stock_data}
News Data: {news_data}

Give a recommendation (BUY/SELL/HOLD), confidence (0-100), and risk level (LOW/MEDIUM/HIGH).
"""

        body = {
            "messages": [{"role": "user", "content": prompt}],
            "model": self.model,
            "temperature": 0.7
        }

        response = httpx.post("https://api.groq.com/openai/v1/chat/completions",
                              headers=headers,
                              json=body)

        resp_json = response.json()

    
        print("Groq Response:", resp_json)

        if "choices" in resp_json:
                reply = resp_json["choices"][0]["message"]["content"]
                return reply
        elif "error" in resp_json:
                return f"❌ API Error: {resp_json['error']['message']}"
        else:
                return "❌ Unexpected response from Groq API"
        print(f"Status code: {response.status_code}")

