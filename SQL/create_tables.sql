USE LoanAnalyticsDW;
GO

CREATE TABLE Dim_Customer (
    Customer_Key INT IDENTITY(1,1) PRIMARY KEY,
    Customer_ID INT,
    Customer_Name VARCHAR(100),
    City VARCHAR(100),
    State VARCHAR(100),
    Age INT
);

CREATE TABLE Dim_Risk (
    Risk_Key INT IDENTITY(1,1) PRIMARY KEY,
    Risk_Level VARCHAR(50)
);

CREATE TABLE Dim_Date (
    Date_Key INT PRIMARY KEY,
    Full_Date DATE,
    Year INT,
    Month INT,
    Day INT
);

CREATE TABLE Fact_Loans (
    Loan_Key INT IDENTITY(1,1) PRIMARY KEY,
    Customer_Key INT,
    Date_Key INT,
    Risk_Key INT,
    Income FLOAT,
    Credit_Score INT,
    Loan_Amount FLOAT,
    Default_Status VARCHAR(10)
);

CREATE TABLE Fact_Reviews (
    Review_Key INT IDENTITY(1,1) PRIMARY KEY,
    Customer_ID INT,
    Review_Text VARCHAR(MAX),
    Review_Date DATE,
    Sentiment VARCHAR(50),
    Risk_Flag VARCHAR(10),
    AI_Summary VARCHAR(MAX)
);