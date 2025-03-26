use msdb;

-- CREATE TABLE AND STORE 3 VALUES
CREATE TABLE Employees (
    EmpID INT NOT NULL PRIMARY KEY IDENTITY(1,1),
    Name VARCHAR(100) NOT NULL,
    Age INT,
    Department VARCHAR(50),
    Salary DECIMAL(10,2)
);

INSERT INTO Employees VALUES
('DHONI',43,'HR','40000000'),
('KOHLI',37,'Team Lead','87000000'),
('PANT',26,'Fresher','600000');

SELECT * FROM Employees;

INSERT INTO Employees VALUES 
('Alice Johnson', 30, 'HR', 45000.00),
('Bob Smith', 40, 'IT', 55000.00),
('Charlie Brown', 28, 'Finance', 50000.00);


-- UPDATE DATE 
UPDATE Employees SET Salary = Salary * 1.10 WHERE Department = 'HR';


--DELETING A DATA
DELETE Employees WHERE Department = 'IT';


--Manipulating Data in Tables 
INSERT INTO Employees VALUES 
('Rahul', 56 , 'IT',35000);

UPDATE Employees SET Department = 'Senior Staff' WHERE SALARY > 50000;

DELETE Employees WHERE AGE > 60;


--Retrieving Specific Attributes 
SELECT NAME,Salary FROM Employees;

SELECT * FROM Employees WHERE Department = 'HR' AND Salary > 50000;

SELECT * FROM Employees ORDER BY Salary DESC;


--Filtering Data - WHERE Clauses 
SELECT EmpID, Name, Age FROM Employees WHERE Age > 30 ORDER BY Age;

SELECT * FROM Employees WHERE Department = 'HR' OR Department = 'Finance';


--Filtering Data - Operators 
SELECT * FROM Employees WHERE Salary BETWEEN 30000 AND 60000;

SELECT * FROM Employees WHERE Name LIKE 'A%';

SELECT * FROM Employees WHERE Department <> 'IT';

SELECT * FROM Employees WHERE Department IN ('Sales','Marketing');

SELECT DISTINCT Department FROM Employees;


-- Column & Table Aliases 
SELECT EmpID as ID , Name , Salary as 'Monthly Income' FROM Employees;


--Filtering Data 
SELECT * FROM Employees WHERE Name LIKE '%JOHN%' AND Salary > 40000;









