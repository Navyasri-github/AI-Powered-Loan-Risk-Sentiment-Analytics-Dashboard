USE LoanAnalyticsDW;
GO
CREATE TABLE Dim_Employment (
    Employment_Key INT IDENTITY(1,1) PRIMARY KEY,
    Employment_Status VARCHAR(50)
);

INSERT INTO Dim_Employment (Employment_Status)
SELECT DISTINCT Employment_Status
FROM Fact_Loans_Edited;

CREATE TABLE Dim_CreditScoreBand (
    CreditScoreBand_Key INT IDENTITY(1,1) PRIMARY KEY,
    CreditScore_Band VARCHAR(50)
);

INSERT INTO Dim_CreditScoreBand (CreditScore_Band)
SELECT DISTINCT 
    CASE 
        WHEN Credit_Score < 600 THEN 'High Risk'
        WHEN Credit_Score < 700 THEN 'Medium Risk'
        ELSE 'Low Risk'
    END
FROM Fact_Loans_Edited;