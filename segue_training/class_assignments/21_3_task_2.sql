-- To FInd the Path
SELECT SERVERPROPERTY('InstanceDefaultDataPath') AS DefaultDataPath;

--Create EmployeeRecords Database with Specific File Paths
CREATE DATABASE EmployeeRecords  
ON (NAME = EmployeeRecords_Data,  
    FILENAME = 'C:\Users\sjlak\OneDrive\Documents\MSSQL16.SQLEXPRESS01\MSSQL\DATA\EmployeeRecords.mdf')  
LOG ON (NAME = EmployeeRecords_Log,  
    FILENAME = 'C:\Users\sjlak\OneDrive\Documents\MSSQL16.SQLEXPRESS01\MSSQL\DATA\EmployeeRecords.ldf');  

--Rename EmployeeRecords to HR_Database
ALTER DATABASE EmployeeRecords MODIFY NAME = HR_Database;  

--Drop HR_Database Safely
DROP DATABASE HR_Database;

--Common SQL Server Data Types & Use Cases
SELECT * FROM sys.types ORDER BY name;

--Create Customers Table
CREATE TABLE Customers (  
    CustomerID INT PRIMARY KEY IDENTITY(1,1),  
    FullName VARCHAR(100),  
    Email VARCHAR(100) UNIQUE,  
    Phone VARCHAR(15),  
    DateJoined DATE  
);  

--Add Address Column
ALTER TABLE Customers ADD Address VARCHAR(255);  

--Rename Customers Table to ClientDetails
EXEC sp_rename 'Customers', 'ClientDetails';  

--Drop ClientDetails Table Safely
DROP TABLE IF EXISTS ClientDetails;  

CREATE TABLE Customers (
    StudentID INT NOT NULL PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT,
    Department VARCHAR(45),
    Email VARCHAR(55)
);

-- Insert Five Sample Records
INSERT INTO Customers  VALUES  
(1,'Harish', 'S', 20, 'Computer Science', 'hharish@gmail.com'),
(2,'anshul', 'kamboj', 22, 'Business', 'fasttrain@yahoo.com'),
(3,'sameer', 'risvi', 19, 'Engineering', 'sixhitter@outlook.com'),
(4,'axar', 'patel', 21, 'Mathematics', 'spinetheball@yahoo.com'),
(5,'Charlie', 'David', 23, 'Physics', 'smashtheball@gmail.com'); 

--Update the email of a customer whose CustomerID = 3
UPDATE Customers SET Email = 'james.new@email.com' WHERE StudentID = 3;  

--Delete a customer record where the CustomerID = 5.
DELETE FROM Customers WHERE StudentID = 5;  

--inserting multiple records in a single query
INSERT INTO Customers  VALUES  
(6,'John', 'cena', 16, 'wrestling', 'youcantseeme@wwe.com'),
(7,'peter', 'parker', 17, 'physics', 'spiderman@stark.com');

--Retrieve and display only the FullName and Email of all customers
SELECT FirstName, Email FROM Customers;  

--Retrieve all customers who joined after 2020-01-01. changed date to age because of table structure
SELECT * FROM Customers WHERE age > 20 ;  

--Fetch all customers whose names start with 'J' using a LIKE query.
SELECT * FROM Customers WHERE FirstName LIKE 'J%';

--Retrieve customers where Email is NULL
SELECT * FROM Customers WHERE Email IS NULL; 

--Filter customers using IN—Retrieve records where CustomerID is either 1, 3, or 7.
SELECT * FROM Customers WHERE StudentID IN (1, 3, 7);  

--Use DISTINCT to list unique domain names from customer emails (e.g., gmail.com, yahoo.com).
SELECT DISTINCT RIGHT(Email, LEN(Email) - CHARINDEX('@', Email)) AS Domain  
FROM Customers;  

--Use AND and OR together—Retrieve customers 
SELECT * FROM Customers  WHERE Department = 'wrestling' OR age < '20';  

--Retrieve customers where and using between
SELECT * FROM Customers WHERE age BETWEEN '20' AND '25';  

--Use column and table aliases to rename output fields while selecting.
SELECT FirstName AS Name, Email AS ContactInfo FROM Customers AS C;  

--Demonstrate a query that filters using multiple conditions
SELECT * FROM Customers WHERE age < '21' AND Department = 'Business';  

--Execute and analyze filtering queries to optimize performance using EXPLAIN plans (if applicable).
SET SHOWPLAN_ALL ON;  
SELECT * FROM Customers WHERE FirstName LIKE 'J%';  
SET SHOWPLAN_ALL OFF;  



























 



