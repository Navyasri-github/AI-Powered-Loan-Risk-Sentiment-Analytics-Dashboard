USE LoanAnalyticsDW;
GO

DECLARE @StartDate DATE = '2023-01-01'
DECLARE @EndDate DATE = '2026-12-31'

WHILE @StartDate <= @EndDate
BEGIN
    INSERT INTO Dim_Date
    VALUES (
        CONVERT(INT, FORMAT(@StartDate, 'yyyyMMdd')),
        @StartDate,
        YEAR(@StartDate),
        MONTH(@StartDate),
        DAY(@StartDate)
    )
    SET @StartDate = DATEADD(DAY, 1, @StartDate)
END