--list all database
SELECT NAME FROM sys.databases;

--query to retrieve the physical file locations (MDF & LDF) of a database named "CompanyDB".
SELECT name, physical_name, type_desc FROM sys.master_files WHERE database_id = DB_ID('CompanyDB');

--TO find default storage path
SELECT SERVERPROPERTY('InstanceDefaultDataPath') AS DataPath,
       SERVERPROPERTY('InstanceDefaultLogPath') AS LogPath;

--query to create a database "HRDB" 
CREATE DATABASE HRDB
ON (NAME = HRDB_Data, 
    FILENAME = 'C:\Users\sjlak\OneDrive\Documents\MSSQL16.SQLEXPRESS01\MSSQL\DATA\HRDB.mdf', 
    SIZE = 10MB, 
    FILEGROWTH = 2MB)
LOG ON (NAME = HRDB_Log, 
    FILENAME = 'C:\Users\sjlak\OneDrive\Documents\MSSQL16.SQLEXPRESS01\MSSQL\DATA\HRDB.ldf', 
    SIZE = 5MB, 
    FILEGROWTH = 1MB);


--Rename "HRDB" to "EmployeeDB" using SQL commands
ALTER DATABASE HRDB MODIFY NAME = EmployeeDB;

--Drop the database "EmployeeDB" from the system.
DROP DATABASE EmployeeDB;

--query to display all supported data types in MS SQL Server.
exec sp_datatype_info;

--Create a table "Employees"
CREATE TABLE Employees2 (
EMPID INT NOT NULL PRIMARY KEY,
EMPName VARCHAR(100) NOT NULL,
JoinDate DATE NOT NULL,
 Salary DECIMAL(10,2) DEFAULT 30000.00
 );

--Add a new column "Department" (VARCHAR(50)) to the "Employees" table.
ALTER TABLE Employees2 ADD Department VARCHAR(50);

--Rename the table "Employees" to "Staff".
EXEC sp_rename 'Employees2','Staff';

--Drop the table "Staff" from the database.
DROP TABLE Staff;






