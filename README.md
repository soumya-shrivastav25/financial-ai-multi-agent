<<<<<<< HEAD

# AI Financial Analyst

An AI-powered financial research and analysis tool that uses the CrewAI framework and Groq's LLaMA 3 model to gather the latest market trends and recommend investment opportunities.

##  Features
- Gathers up-to-date financial news and stock trends.
- Analyzes research to give actionable investment recommendations.
- Modular design with Agents and Tasks using CrewAI.
- Runs on Groq's blazing-fast LLaMA 3 API.

---

##  Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# Install dependencies
pip install -r requirements.txt
````

---

##  Setup

1. Create a `.env` file in the project root.
2. Add your Groq API key to it:

   ```
   GROQ_API_KEY=your_api_key_here
   ```
3. Ensure your API key is from [Groq](https://groq.com).

---

## ▶ Run

```bash
python ai_financial_analyst.py
```

---

##  Example Output

```
Final Output:

1. Microsoft Corporation (MSFT)
   Microsoft has been a consistent performer in the tech sector, driven by its dominant positions in software, gaming, and cloud computing. Its Azure cloud platform has seen significant growth, and its AI/ML capabilities are increasingly adopted by businesses.

2. NVIDIA Corporation (NVDA)
   NVIDIA is a leader in GPUs with strong diversification into AI, data centers, and gaming. Its strategic acquisitions have expanded its presence in the data center market.

3. Salesforce.com, Inc. (CRM)
   Salesforce leads the CRM market with a robust cloud platform, rapid adoption, and strong innovation, making it attractive for long-term growth.
```

---

##  Project Structure

```
AI_Financial_Analyst/
├── ai_financial_analyst.py   # Main script
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (not committed)
└── README.md                 # Project documentation
```

---

=======
# financial-ai-multi-agent
Multi-agent AI system for financial research &amp; stock recommendations using CrewAI and Groq API
>>>>>>> 443401f6d1d2f3e3c577994bb0134c2d6b3fbcdc
