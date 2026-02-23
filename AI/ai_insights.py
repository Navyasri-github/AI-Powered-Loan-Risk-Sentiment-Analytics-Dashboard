import os
import pyodbc
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

try:
    load_dotenv()

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    conn = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=LAPTOP-55AU0487;"
        "DATABASE=SalesDB;"
        "Trusted_Connection=yes;"
    )

    query = """
    SELECT TOP 20 ProductName, SUM(SalesAmount) as TotalSales
    FROM Sales
    GROUP BY ProductName
    ORDER BY TotalSales DESC
    """

    df = pd.read_sql(query, conn)

    data_text = df.to_string(index=False)

    prompt = f"""
    You are a Senior Business Data Analyst.

    Analyze the following sales data and provide:
    - Revenue trends
    - Risk alerts
    - Growth opportunities
    - Executive summary

    Data:
    {data_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert business analyst."},
            {"role": "user", "content": prompt}
        ]
    )

    insight_text = response.choices[0].message.content

    cursor = conn.cursor()

    insert_query = """
    INSERT INTO AI_Insights (InsightText)
    VALUES (?)
    """

    cursor.execute(insert_query, insight_text)
    conn.commit()

    print(f"Success: Insights generated at {datetime.now()}")

    conn.close()

except Exception as e:
    print("Error occurred:", str(e))