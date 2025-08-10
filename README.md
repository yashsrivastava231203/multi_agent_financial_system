# Multi-Agent Financial Analysis System
A Python-based modular multi-agent system that fetches, analyzes, and interprets financial data using coordinated agent workflows to deliver investment insights.
## 📂 Project Structure
project/
│
├── financial_analysis.py # Main entry point
├── venv/ # Python virtual environment (not uploaded to GitHub)
└── financial_analysis/
├── init.py
├── analysis.py # Performs data analysis & technical computations
├── config.py # Stores configuration values and constants
├── logging.py # Centralized logging setup
├── utils.py # Helper functions
│
├── agents/
│ ├── data_fetcher.py # Fetches financial data from APIs (e.g., yfinance)
│ ├── expert_agent.py # Provides investment recommendations based on analysis
│ ├── news_agent.py # Fetches and summarizes latest financial news
│ └── coordinator.py # Coordinates communication between all agents

## ⚙️ Features

- **Multi-Agent Architecture**  
  Separate agents for data fetching, news summarization, expert recommendations, and coordination.

- **Data Fetching**  
  Pulls stock market and company data from APIs such as `yfinance`.

- **Automated Analysis**  
  Computes technical indicators, valuations, and insights for investment decisions.

- **Financial News Summarization**  
  Fetches and summarizes relevant market news for context.

- **Expert Advisory**  
  Generates actionable buy/hold/sell recommendations.


## 🛠 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/multi-agent-financial-analysis.git
   cd multi-agent-financial-analysis
2. **Create and activate virtual environment**
    ```bash
    python -m venv venv
  # On Windows:
    venv\Scripts\activate
  # On macOS/Linux:
    source venv/bin/activate
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt

## 🚀 Usage
Run the main script: python financial_analysis.py
This will:
1. Trigger the CoordinatorAgent.
2. Fetch real-time stock data and market news.
3. Perform analysis and compute technical indicators.
4. Generate summarized insights and recommendations.

## 🧩 Agent Responsibilities
DataFetcherAgent: Connects to APIs, retrieves historical and real-time data.
NewsAgent: Pulls relevant news headlines and summarizes key points.
ExpertAgent: Analyzes data trends, applies investment strategies, outputs recommendations.
CoordinatorAgent: Manages workflow, ensures smooth interaction between agents.

## 📚 Publication
This system is described in the research paper: International Journal of Engineering and Technology (IJET), Volume 11 Issue 4 (2025), titled “Multi-Agent Financial Analysis System: From Real-Time Data Fetching to Expert Advisory.” 




