
--SQL query that dynamically renames the SalesAmount column based on the current month
CREATE TABLE SalesData (
    SalesID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    SalesAmount DECIMAL(10,2),
    SalesDate DATE
);

INSERT INTO SalesData (SalesID, ProductName, SalesAmount, SalesDate)
VALUES
(1, 'Laptop', 1200.50, '2025-03-10'),
(2, 'Smartphone', 800.75, '2025-03-15'),
(3, 'Tablet', 450.30, '2025-03-20');

DECLARE @sql NVARCHAR(MAX);
DECLARE @monthName NVARCHAR(20);
SET @monthName = DATENAME(MONTH, GETDATE());
SET @sql = 
    'SELECT SalesID, ProductName, SalesAmount AS Sales_' + @monthName + ', SalesDate FROM SalesData;';

EXEC sp_executesql @sql;


--SQL query to pivot the data so that the result displays one row per employee with separate columns for each month's salary 

CREATE TABLE EmployeeSalary2 (
    EmployeeID INT ,
    EmployeeName VARCHAR(100),
    SalaryMonth VARCHAR(15),  
    SalaryAmount DECIMAL(10,2)
);

INSERT INTO EmployeeSalary2 VALUES
(1, 'Alice', 'January', 5000.00),
(1, 'Alice', 'February', 5200.00),
(1, 'Alice', 'March', 5300.00),
(2, 'Bob', 'January', 4800.00),
(2, 'Bob', 'February', 4900.00),
(2, 'Bob', 'March', 4950.00);

select * from EmployeeSalary2;

SELECT * 
FROM (
    SELECT EmployeeID, EmployeeName, SalaryMonth, SalaryAmount
    FROM EmployeeSalary2
) AS SourceTable
PIVOT (
    MAX(SalaryAmount) 
    FOR SalaryMonth IN ([January], [February], [March], [April], [May], [June], 
                        [July], [August], [September], [October], [November], [December])
) AS PivotTable;


--SQL query to return the top 3 transactions per customer, ranked by TransactionAmount in descending order. 
--If two transactions have the same amount, order them by TransactionDate in descending order.

CREATE TABLE CustomerTransactions (
    TransactionID INT PRIMARY KEY,
    CustomerID INT, 
    TransactionAmount DECIMAL(10,2),
    TransactionDate DATE
);

INSERT INTO CustomerTransactions (TransactionID, CustomerID, TransactionAmount, TransactionDate)
VALUES
(1, 101, 500.00, '2025-03-01'),
(2, 101, 700.00, '2025-03-05'),
(3, 101, 600.00, '2025-03-03'),
(4, 101, 700.00, '2025-03-06'),
(5, 101, 800.00, '2025-03-07'),
(6, 102, 400.00, '2025-03-02'),
(7, 102, 900.00, '2025-03-10'),
(8, 102, 450.00, '2025-03-08'),
(9, 102, 500.00, '2025-03-12'),
(10, 102, 550.00, '2025-03-15');

WITH RankedTransactions AS (
    SELECT 
        TransactionID,
        CustomerID,
        TransactionAmount,
        TransactionDate,
        ROW_NUMBER() OVER (
            PARTITION BY CustomerID 
            ORDER BY TransactionAmount DESC, TransactionDate DESC
        ) AS Rank
    FROM CustomerTransactions
)
SELECT TransactionID, CustomerID, TransactionAmount, TransactionDate
FROM RankedTransactions
WHERE Rank <= 3
ORDER BY CustomerID, Rank;

---can do it using rank too 
WITH RankedTransactions AS (
    SELECT 
        TransactionID,
        CustomerID,
        TransactionAmount,
        TransactionDate,
        DENSE_RANK() OVER (
            PARTITION BY CustomerID 
            ORDER BY TransactionAmount DESC, TransactionDate DESC
        ) AS Rank
    FROM CustomerTransactions
)
SELECT TransactionID, CustomerID, TransactionAmount, TransactionDate
FROM RankedTransactions
WHERE Rank <= 3
ORDER BY CustomerID, Rank;


--SQL query to return a summary of total OrderAmount per customer. Additionally, add separate columns for TotalOrdersThisYear and TotalOrdersLastYear.

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT, 
    OrderAmount DECIMAL(10,2),
    OrderDate DATE
);

INSERT INTO Orders (OrderID, CustomerID, OrderAmount, OrderDate)
VALUES
(1, 101, 500.00, '2024-03-10'),
(2, 101, 700.00, '2023-05-15'),
(3, 101, 600.00, '2024-07-20'),
(4, 102, 900.00, '2024-02-10'),
(5, 102, 800.00, '2023-08-25'),
(6, 103, 1000.00, '2023-06-14'),
(7, 103, 1200.00, '2024-01-05');

SELECT 
    CustomerID,
    SUM(OrderAmount) AS TotalOrderAmount,
    SUM(CASE WHEN YEAR(OrderDate) = YEAR(GETDATE()) THEN OrderAmount ELSE 0 END) AS TotalOrdersThisYear,
    SUM(CASE WHEN YEAR(OrderDate) = YEAR(GETDATE()) - 1 THEN OrderAmount ELSE 0 END) AS TotalOrdersLastYear
FROM Orders
GROUP BY CustomerID
ORDER BY CustomerID;



--SQL query that assigns a rank to each student per subject based on their Score. If two students have the same score, 
--they should receive the same rank, and the next rank should be adjusted accordingly (e.g., using DENSE_RANK()).

CREATE TABLE StudentScores (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100),
    Subject VARCHAR(50),
    Score INT
);

INSERT INTO StudentScores (StudentID, StudentName, Subject, Score)
VALUES
(1, 'Alice', 'Math', 95),
(2, 'Bob', 'Math', 90),
(3, 'Charlie', 'Math', 95),
(4, 'David', 'Math', 85),
(5, 'Alice', 'Science', 88),
(6, 'Bob', 'Science', 92),
(7, 'Charlie', 'Science', 88),
(8, 'David', 'Science', 80);

SELECT Subject, StudentID, StudentName, Score, DENSE_RANK() 
OVER (PARTITION BY Subject ORDER BY Score DESC) AS Rank
FROM StudentScores ORDER BY Subject, Rank;







