import os
from dotenv import load_dotenv

load_dotenv()

def get_config():
    return {
        "OPENAI_API_KEY": os.getenv("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"),
        "POLYGON_API_KEY": os.getenv("mYYp0zIeRyF3bxi_r2g90aHNWmUbC0ZO"),
        "NEWS_API_KEY": os.getenv("3000afe5b9574c31ba6bbf38da208297")
    }
