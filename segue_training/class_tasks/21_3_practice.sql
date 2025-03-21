USE Foundationtraining;

SELECT TeamCaptain as TC, TOPSCORE FROM IPL;

SELECT * FROM IPL ORDER BY TOPSCORE DESC;

SELECT TOP 2 * FROM IPL;

SELECT TOPSCORE , COUNT(*) AS COUNT FROM IPL GROUP BY TOPSCORE;


--Scenario:
--A company maintains an Employees database, storing employee details in the following table:

CREATE TABLE Employees (

    EmployeeID INT PRIMARY KEY,

    FirstName NVARCHAR(50),

    LastName NVARCHAR(50),

    DateOfBirth DATE,

    HireDate DATE,

    Salary DECIMAL(10,2),

    Department NVARCHAR(50)

);


INSERT INTO Employees VALUES
(1,'Ram','shankar','2001-12-12','2024-12-23',1200000,'AI');

SELECT * FROM Employees;

INSERT INTO Employees VALUES  
(2, 'Sita', 'Verma', '1998-05-20', '2023-11-15', 900000, 'HR'),  
(3, 'Amit', 'Kumar', '1995-08-10', '2022-07-01', 1500000, 'Finance'),  
(4, 'Neha', 'Singh', '1997-02-25', '2021-03-10', 800000, 'Marketing'),  
(5, 'Vikram', 'Gupta', '1993-09-18', '2019-06-20', 1700000, 'IT'),  
(6, 'Pooja', 'Sharma', '1999-04-14', '2020-09-05', 950000, 'Sales'),  
(7, 'Rahul', 'Yadav', '1996-11-30', '2018-12-01', 1350000, 'Operations'),  
(8, 'Ananya', 'Chopra', '2000-07-07', '2025-01-10', 1100000, 'AI'),  
(9, 'Karan', 'Malhotra', '1994-06-22', '2017-04-30', 1800000, 'Engineering'),  
(10, 'Meera', 'Rao', '1992-01-10', '2015-08-15', 2000000, 'Management');  


--Write a query that combines FirstName and LastName into a single column named FullName (Format: "LastName, FirstName").
SELECT EmployeeID , CONCAT(LastName,',',FirstName) AS FULLNAME FROM Employees;

--Add a column named Age that calculates the employee's age using the DateOfBirth field.
SELECT EmployeeID, FirstName, LastName, DATEDIFF(YEAR, DateOfBirth, GETDATE()) AS Age FROM Employees;

--Add a column named YearsOfService that calculates how many years an employee has worked in the company based on HireDate.
SELECT EmployeeID, DATEDIFF(YEAR,HireDate, GETDATE()) AS YearOfServices FROM Employees;

--Create a new column named SalaryCategory that classifies employees into:
--'Low' if Salary < 50,000
--'Medium' if Salary between 50,000 and 100,000
--'High' if Salary > 100,000
SELECT EmployeeID, Salary, 
       CASE  
           WHEN Salary < 50000 THEN 'LOW'  
           WHEN Salary BETWEEN 50000 AND 100000 THEN 'MEDIUM'  
           ELSE 'HIGH'  
       END AS SalaryCategory 
FROM Employees;


--Display the full name of the month in which the employee was hired using a SQL function.
SELECT EmployeeID, FirstName, LastName, DATENAME(MONTH, HireDate) AS JoiningMonth FROM Employees;



SELECT LEN('delhi capitals')
SELECT UPPER ('kingkong')
SELECT SUBSTRING ('virat kohli',2,6)
SELECT LEFT('harish',3)
SELECT RIGHT('harish',3)

select len('Bhavna Joshi');
select upper('Bhavna Joshi');
select Substring('Bhavna Joshi',5,10);
 
select left ('Database training',4);
select right ('Database training',4);
select charindex ('t','Database training');
select replace('Hello team, how are you','team','çandidates');
select stuff('Hello team, how are you',7,17,'developers');
 
select LTRIM('HHHHello') as TrimmedLeft ,RTRIM('Teamsss') as TrimmedRight;
 
select CONCAT('Hello',' ','Developers') as myname;
select STRING_AGG(TeamName, ',') from IPL;
select STRING_AGG(FirstName, ',') from Employees;

SELECT FORMAT(GETDATE(),'yyyy-mm-dd') as FORMAT;

SELECT FORMAT(GETDATE(),'dddd MMMM dd,yyyy') as new;

select format(getdate(),'dd-MM-yyyy') ;

SELECT Department, SUM(Salary) AS TotalSalary
FROM Employees
GROUP BY ROLLUP(Department);

SELECT Department, DATENAME(MONTH, HireDate) AS JoiningMonth, SUM(Salary) AS TotalSalary
FROM Employees
GROUP BY CUBE(Department, DATENAME(MONTH, HireDate));

