CREATE DATABASE Foundationtraining;



CREATE TABLE IPL(
TeamID int not null primary key,
TeamName varchar(60),
TeamOwner varchar(75),
TeamCaptain varchar (75)
);

SELECT * FROM sys.databases;

SELECT * FROM IPL;

INSERT INTO IPL VALUES (
1, 'RCB', 'Diageo', 'Rajat'),
(5,'DC', 'GMR', 'Axar'),
(3, 'CSK','India cements','Ruturaj'),
(4,'KKR','Shah Rukh Khan','Rahanane');

SELECT * FROM IPL;



CREATE TABLE FOOD(
OrderID INT not null PRIMARY KEY,
Cuisine VARCHAR(45),
Item VARCHAR(55),
DeliveryType VARCHAR(30)
);

INSERT INTO FOOD VALUES (
1,'INDIAN','NAAN','DINEIN'),
(2,'MEXICAN','PASTA','TAKEAWAY');

SELECT * FROM FOOD;


CREATE DATABASE MSSQL;

use Foundationtraining;

use MSSQL;

ALTER DATABASE MSSQL MODIFY NAME = SEGUE;

ALTER DATABASE SEGUE SET OFFLINE;

ALTER DATABASE SEGUE SET ONLINE;

ALTER DATABASE SEGUE SET MULTI_USER;

USE Foundationtraining;

DROP DATABASE SEGUE;

USE SEGUE;

USE Foundationtraining;

ALTER DATABASE Foundationtraining SET READ_ONLY;

INSERT INTO IPL VALUES (
6,'LSG' , 'GOENKA', 'PANT');

ALTER DATABASE Foundationtraining SET READ_WRITE;

INSERT INTO IPL VALUES (
7,'MI' , 'AMBANI', 'HARDIK');

SELECT * FROM IPL;

CREATE TABLE MARKS (
StuName VARCHAR(50),
SubName VARCHAR(20),
TotalMarks INT
);

INSERT INTO MARKS VALUES(
'HARISH', 'SQL', 65),
('RAM', 'SQL', 45);

INSERT INTO MARKS VALUES(
'KAMAL', 'SQL', 85),
('RUTU', 'SQL', 56);

SELECT * FROM MARKS;

SELECT MAX(TotalMarks) FROM MARKS;


SELECT * FROM MARKS WHERE TotalMarks = (SELECT MAX(TotalMarks) FROM MARKS);
SELECT StuName FROM MARKS WHERE TotalMarks = (SELECT MAX(TotalMarks) FROM MARKS);



CREATE TABLE SCORE (
    Name VARCHAR(100),
    Subject VARCHAR(50),
    Marks INT
);

INSERT INTO SCORE VALUES ('Ram', 'Maths', 90);
INSERT INTO SCORE VALUES ('Ram', 'Science', 85);
INSERT INTO SCORE VALUES ('Babu', 'Maths', 78);
INSERT INTO SCORE VALUES ('Babu', 'Science', 88);
INSERT INTO SCORE VALUES ('Charu', 'Maths', 95);
INSERT INTO SCORE VALUES ('Charu', 'Science', 92);

SELECT Name, SUM(Marks) AS TotalMarks
FROM SCORE
GROUP BY Name;

SELECT Subject, MAX(Marks) AS MaxMarks
FROM SCORE
GROUP BY Subject;

SELECT TOP 1 Name, SUM(Marks) AS TotalMarks
FROM SCORE
GROUP BY Name
ORDER BY TotalMarks DESC;

EXEC sp_help IPL;

select COLUMN_NAME,DATA_TYPE,CHARACTER_MAXIMUM_LENGTH FROM INFORMATION_SCHEMA.COLUMNS where TABLE_NAME= 'IPL';

ALTER TABLE IPL ADD TOPSCORE INT;

SELECT * FROM IPL;

UPDATE IPL SET TOPSCORE = 232 WHERE TeamName = 'RCB';

UPDATE IPL SET TOPSCORE = 200 WHERE TeamName = 'RR';

UPDATE IPL SET TOPSCORE = 212 WHERE TeamName = 'CSK';

UPDATE IPL SET TOPSCORE = 211 WHERE TeamName = 'KKR';

UPDATE IPL SET TOPSCORE = 285 WHERE TeamName = 'DC';

UPDATE IPL SET TOPSCORE = 203 WHERE TeamName = 'LSG';

UPDATE IPL SET TOPSCORE = 199 WHERE TeamName = 'MI';

UPDATE IPL SET TeamName = 'RR' WHERE TeamID = 2;

UPDATE IPL SET TeamOwner = 'Manoj Badale' WHERE TeamID = 2;

SELECT * FROM IPL;

exec sp_rename to rename the table 

DELETE FROM IPL WHERE TOPSCORE < 200;

UPDATE IPL SET TeamCaptain = 'DHONI' WHERE TeamName = 'CSK';

SELECT * FROM IPL;

SELECT TeamName FROM IPL WHERE TOPSCORE > 210;

SELECT * FROM IPL WHERE TeamCaptain in ('pant','DHONI');

SELECT * FROM IPL WHERE TeamCaptain not in ('pant','DHONI');

SELECT * FROM IPL WHERE TOPSCORE BETWEEN 200 AND 210;











 