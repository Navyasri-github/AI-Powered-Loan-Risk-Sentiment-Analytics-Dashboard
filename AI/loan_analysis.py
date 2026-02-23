import openai
import pandas as pd
import os

# Set your OpenAI API key
openai.api_key = ""

# Example loan data
loan_data = [
    {"Loan_ID": 1, "Income": 50000, "Credit_Score": 620, "Loan_Amount": 15000, "Employment_Status": "Employed"},
    {"Loan_ID": 2, "Income": 30000, "Credit_Score": 550, "Loan_Amount": 12000, "Employment_Status": "Self-Employed"},
]

df = pd.DataFrame(loan_data)

# GPT-4 loan analysis
def analyze_loan(row):
    prompt = f"""
    You are a financial risk analyst. Based on this loan profile:

    Income: {row['Income']}
    Credit Score: {row['Credit_Score']}
    Loan Amount: {row['Loan_Amount']}
    Employment Status: {row['Employment_Status']}

    Explain:
    1. Risk category
    2. Why it is risky
    3. Recommendation
    4. Default probability in %
    Be concise and professional.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=250
    )
    return response['choices'][0]['message']['content'].strip()

df['AI_Analysis'] = df.apply(analyze_loan, axis=1)

# Save the output to CSV so Power BI can read it
df.to_csv("loan_analysis_output.csv", index=False)
print("Analysis complete! CSV saved as 'loan_analysis_output.csv'")