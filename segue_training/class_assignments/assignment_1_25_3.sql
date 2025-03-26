-- 1) List all system databases
SELECT name FROM sys.databases;

-- 2) Identify the physical database files of SalesDB
CREATE DATABASE SalesDB;

SELECT name AS LogicalName, physical_name AS PhysicalFilePath, type_desc AS FileType
FROM sys.master_files
WHERE database_id = DB_ID('SalesDB');


-- 3) Create InventoryDB 
CREATE DATABASE InventoryDB;

-- 4) Rename InventoryDB to StockDB
ALTER DATABASE InventoryDB MODIFY NAME = StockDB;

-- 5) Drop StockDB
DROP DATABASE StockDB;

-- 6) Display all available data types in SQL Server
SELECT name FROM sys.types ORDER BY name;

-- 7) Create "Products" table
CREATE TABLE Products1 (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50) NOT NULL,
    Price DECIMAL(10,2),
    StockQuantity INT DEFAULT 0
);

-- 8) Add "Category" column to "Products"
ALTER TABLE Products1 ADD Category VARCHAR(30);

-- 9) Rename "Products" table to "Inventory"
EXEC sp_rename 'Products1', 'Inventory1';

-- 10) Drop "Inventory" table
DROP TABLE Inventory1;

-- 11) List and describe system databases
SELECT * FROM sys.databases;

-- 12) Display all database files (MDF, LDF, NDF) for a specific database
exec sp_help;

-- 13) Create "SalesDB" with a primary data file (10MB) and log file (5MB)
CREATE DATABASE SalesDB1;

-- 14) Rename "SalesDB" to "RetailDB"
ALTER DATABASE SalesDB MODIFY NAME = RetailDB;

-- 15) Drop "RetailDB" safely, ensuring no active connections exist
ALTER DATABASE RetailDB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
DROP DATABASE RetailDB;
