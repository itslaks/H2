CREATE DATABASE PayXpert;

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


