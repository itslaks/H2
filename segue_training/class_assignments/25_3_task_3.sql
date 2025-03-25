CREATE TABLE Organizations (
    OrganizationID INT PRIMARY KEY,
    OrganizationName VARCHAR(100) NOT NULL
);

CREATE TABLE Series (
    SeriesID INT PRIMARY KEY,
    SeriesName VARCHAR(100) NOT NULL,
    TRP DECIMAL NOT NULL,
    NoOfViews INT NOT NULL,
    OrganizationID INT,
    FOREIGN KEY (OrganizationID) REFERENCES Organizations(OrganizationID)
);

CREATE TABLE Cartoons (
    CartoonID INT PRIMARY KEY,
    CartoonName VARCHAR(100) NOT NULL,
    SeriesID INT,
    FOREIGN KEY (SeriesID) REFERENCES Series(SeriesID)
);

EXEC sp_rename 'Cartoons.CartoonName', 'CharacterName', 'COLUMN';

INSERT INTO Organizations VALUES 
(1, 'Marvel'),
(2, 'Cartoon Network'),
(3, 'TV Tokyo'),
(4, 'Shin-Ei Animation'),
(5, 'Fujiko Pro'),
(6, 'Sony Pictures');

SELECT * FROM Organizations;


INSERT INTO Series VALUES 
(1, 'Spider-Man', 8.5, 5000000, 1),
(2, 'Ben 10', 7.9, 4500000, 2),
(3, 'Pokemon', 9.2, 7000000, 3),
(4, 'Shin Chan', 7.5, 4000000, 4),
(5, 'Doraemon', 8.8, 6000000, 5),
(6, 'Jackie Chan Adventures', 8.0, 4800000, 6);

SELECT * FROM Series;

INSERT INTO Cartoons VALUES 
(1, 'Spider-Man', 1),
(2, 'Ben 10', 2),
(3, 'Pikachu', 3),
(4, 'Shin Chan', 4),
(5, 'Doraemon', 5),
(6, 'Jackie Chan', 6);

SELECT * FROM Cartoons;



--TASKS:

SELECT * FROM Series WHERE TRP > 5.0;

SELECT TRP ,SeriesName FROM Series ORDER BY TRP DESC;

SELECT TOP 1 C.CharacterName, S.SeriesName, S.NoOfViews 
FROM Cartoons C 
JOIN Series S ON C.SeriesID = S.SeriesID
ORDER BY S.NoOfViews DESC; 

