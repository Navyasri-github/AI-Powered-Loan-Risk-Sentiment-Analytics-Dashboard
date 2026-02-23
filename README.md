# AI-Powered-Loan-Risk-Sentiment-Analytics-Dashboard

# AI-Powered Loan Risk & Sentiment Analytics Dashboard

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT4-purple)](https://platform.openai.com/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-orange)](https://powerbi.microsoft.com/)

---

## Description
This project is an **AI-powered loan risk analytics platform** that uses **OpenAI GPT-4** to evaluate loans and generate actionable insights for financial decision-making.  

For each loan, the platform provides:
- Risk category (High / Medium / Low)  
- Explanation of why the loan is risky  
- Recommendation  
- Default probability (%)  

Results are visualized in **Power BI** with **interactive KPIs, charts, and slicers**, enabling loan officers or analysts to quickly identify high-risk loans and make informed decisions.

---

## Features
- Automated GPT-4 risk analysis for each loan  
- Interactive Power BI dashboard:
  - Risk distribution charts  
  - KPI cards: Average Default Probability, Count of High-Risk Loans  
  - Filters by Employment Status, Credit Score, Loan Amount  
- Optional sentiment analysis for customer feedback  
- Fully customizable and extendable  

---

## Project Workflow

1. **Prepare Loan Data**  
   - Load loan dataset using Python and Pandas.

2. **GPT-4 Risk Analysis**  
   - Python script calls the OpenAI API to analyze each loan profile.  

3. **Parse AI Output**  
   - Split GPT output into:
     - `Risk Category`
     - `Recommendation`
     - `Default Probability`  

4. **Export CSV**  
   - Save AI analysis results to a CSV file (`loan_analysis_output.csv`) for Power BI.

5. **Power BI Dashboard**  
   - Load CSV in Power BI.  
   - Create Table visuals, KPI Cards, Pie/Bar Charts, and interactive Slicers.  

6. **Automation (Optional)**  
   - Schedule Python script to update CSV daily and refresh Power BI dashboard automatically.  

---

