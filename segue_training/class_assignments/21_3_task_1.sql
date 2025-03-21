--Write an SQL script to create a database named StudentRecords.
CREATE DATABASE StudentRecords;

--Rename the StudentRecords database to UniversityRecords.
ALTER DATABASE StudentRecords MODIFY NAME = UniversityRecords;

--Delete the UniversityRecords database safely.
DROP DATABASE IF EXISTS UniversityRecords;

--List and describe common SQL Server data types
SELECT * FROM sys.types ORDER BY name;

--Create a Students table with appropriate columns and data types
CREATE TABLE Students (
    StudentID INT PRIMARY KEY IDENTITY(1,1),
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT,
    Department VARCHAR(100)
);

--  Add a new column Email to the Students table
ALTER TABLE Students ADD Email VARCHAR(100);

-- Rename the Students table to UniversityStudents
EXEC sp_rename 'Students', 'UniversityStudents';

-- Delete the UniversityStudents table
DROP TABLE IF EXISTS UniversityStudents;

--  Recreate the Students table for inserting records
CREATE TABLE Students (
    StudentID INT NOT NULL PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT,
    Department VARCHAR(45),
    Email VARCHAR(55)
);

--Insert five sample student records into the Students table
INSERT INTO Students VALUES
(1,'Harish', 'S', 20, 'Computer Science', 'hharish@gmail.com'),
(2,'anshul', 'kamboj', 22, 'Business', 'fasttrain@yahoo.com'),
(3,'sameer', 'risvi', 19, 'Engineering', 'sixhitter@outlook.com'),
(4,'axar', 'patel', 21, 'Mathematics', 'spinetheball@yahoo.com'),
(5,'Charlie', 'David', 23, 'Physics', 'smashtheball@gmail.com');

--  Update the email of a specific student
UPDATE Students SET Email = 'aidsdon@vsbec.com' WHERE StudentID = 1;


--Delete a record of a student who has graduated 
DELETE FROM Students WHERE Age > 22;

--Select and display only the names and emails of students
SELECT FirstName, LastName, Email FROM Students;

INSERT INTO Students  VALUES
(6,'John', 'cena', 16, 'wrestling', 'youcantseeme@wwe.com'),
(7,'peter', 'parker', 17, 'physics', 'spiderman@stark.com');

--Retrieve students based on a specific condition 
SELECT * FROM Students WHERE Age > 18;

--Fetch all records from the table
SELECT * FROM Students;

--Retrieve students who belong to a specific department.
SELECT * FROM Students WHERE Department = 'wrestling';

--queries to demonstrate filtering
SELECT * FROM Students WHERE Department IN ('Computer Science', 'Physics');

SELECT DISTINCT Age FROM Students;

SELECT * FROM Students WHERE Age > 18 AND Department = 'Engineering';

SELECT * FROM Students WHERE Age < 20 OR Department = 'Mathematics';

SELECT * FROM Students WHERE Age BETWEEN 19 AND 22;

SELECT * FROM Students WHERE FirstName LIKE 'H%';

SELECT FirstName AS Name, Email AS Contact FROM Students;

