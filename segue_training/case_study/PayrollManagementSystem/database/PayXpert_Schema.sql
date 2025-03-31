CREATE DATABASE PayXpert;
USE PayXpert;

CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY IDENTITY(1,1),
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    DateOfBirth DATE,
    Gender NVARCHAR(10),
    Email NVARCHAR(100) UNIQUE,
    PhoneNumber NVARCHAR(15),
    Address NVARCHAR(255),
    Position NVARCHAR(50),
    JoiningDate DATE,
    TerminationDate DATE NULL
);

CREATE TABLE Payroll (
    PayrollID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT FOREIGN KEY REFERENCES Employee(EmployeeID),
    PayPeriodStartDate DATE,
    PayPeriodEndDate DATE,
    BasicSalary DECIMAL(10,2),
    OvertimePay DECIMAL(10,2),
    Deductions DECIMAL(10,2),
    NetSalary DECIMAL(10,2)
);

CREATE TABLE Tax (
    TaxID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT FOREIGN KEY REFERENCES Employee(EmployeeID),
    TaxYear INT,
    TaxableIncome DECIMAL(10,2),
    TaxAmount DECIMAL(10,2)
);

CREATE TABLE FinancialRecord (
    RecordID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT FOREIGN KEY REFERENCES Employee(EmployeeID),
    RecordDate DATE,
    Description NVARCHAR(255),
    Amount DECIMAL(10,2),
    RecordType NVARCHAR(50)
);




INSERT INTO Employee VALUES
('Meg', 'Ner', '1990-05-12', 'Male', 'megalaaxis@gmail.com', '9876543210', 'Bangalore, India', 'Software Engineer', '2020-03-15', NULL),
('Rithesh', 'Naga', '1985-08-23', 'Male', 'rithesh@yahoo.com', '9865321470', 'Chennai, India', 'Project Manager', '2018-07-10', NULL),
('Aadhitya', 'A A', '1992-01-30', 'Male', 'aadhitya@outlook.com', '9987456321', 'Mumbai, India', 'Data Analyst', '2021-06-20', NULL),
('Nandhiithaa', 'L', '1995-04-17', 'Female', 'nandhiithaa@neo.com', '9873214560', 'Kolkata, India', 'HR Manager', '2019-02-25', NULL),
('Harish', 'Shree', '1988-12-09', 'Male', 'harish@kct.com', '9845612378', 'Hyderabad, India', 'Finance Executive', '2017-09-05', NULL),
('Kamalsha', 'K', '1993-07-14', 'Male', 'kamalsha@vsb.com', '9768543120', 'Delhi, India', 'Software Tester', '2022-11-30', NULL);


INSERT INTO Payroll VALUES
(1, '2024-03-01', '2024-03-31', 700000, 50000, 70000, 680000),
(2, '2024-03-01', '2024-03-31', 1200000, 80000, 120000, 1160000),
(3, '2024-03-01', '2024-03-31', 850000, 30000, 85000, 795000),
(4, '2024-03-01', '2024-03-31', 900000, 40000, 90000, 850000),
(5, '2024-03-01', '2024-03-31', 950000, 60000, 95000, 915000),
(6, '2024-03-01', '2024-03-31', 600000, 20000, 60000, 560000);


INSERT INTO Tax VALUES
(1, 2024, 840000, 100800),
(2, 2024, 1440000, 172800),
(3, 2024, 1020000, 122400),
(4, 2024, 1080000, 129600),
(5, 2024, 1140000, 136800),
(6, 2024, 720000, 86400);


INSERT INTO FinancialRecord VALUES
(1, '2024-03-15', 'Health Insurance Deduction', 2000000, 'Credit'),
(2, '2024-03-20', 'Annual Bonus', 5000000, 'Credit'),
(3, '2024-03-25', 'Travel Allowance', 3000000, 'Credit'),
(4, '2024-03-10', 'Salary Advance', -10000, 'Deduction'),
(5, '2024-03-05', 'Loan Repayment', -15000, 'Deduction'),
(6, '2024-03-28', 'Performance Incentive', 700000, 'Credit');
