CREATE TABLE CINEMA (
    cID INT NOT NULL PRIMARY KEY,
    cNAME VARCHAR(78),
    cHERO VARCHAR(50),
    cGENRE VARCHAR(80),
    cRELEASEDATE DATE
);

CREATE TABLE DIRECTORS (
    cID INT NOT NULL,
    dNAME VARCHAR(50) NOT NULL,
    dEXPERIENCE INT,
    FOREIGN KEY (cID) REFERENCES CINEMA(cID)
);

INSERT INTO CINEMA  VALUES
(1, 'DRAGON', 'Pradeep', 'Romance', '2025-02-20'),
(2, 'MASTER', 'Vijay', 'Action', '2022-08-05'),
(6, 'Theri', 'Vijay', 'Action', '2016-04-14'),
(7, '24', 'Suriya', 'Sci-Fi', '2016-05-06'),
(8, 'Petta', 'Rajinikanth', 'Action', '2019-01-10'),
(9, 'Vishwaroopam', 'Kamal Haasan', 'Thriller', '2013-02-07'),
(10, 'Vidamuyarchi', 'Ajith Kumar', 'Action', '2025-02-10'),
(11, 'Hi Nanna', 'Nani', 'Romance', '2023-12-07'),
(12, 'Sita Ramam', 'Dulquer Salmaan', 'Romance', '2022-08-05');

INSERT INTO DIRECTORS VALUES
(6, 'Atlee', 10),
(7, 'Vikram Kumar', 15),
(8, 'Karthik Subbaraj', 12),
(9, 'Kamal Haasan', 40),
(10, 'Magizh Thirumeni', 18),
(11, 'Shouryuv', 5),
(12, 'Hanu Raghavapudi', 12);

SELECT * FROM CINEMA;

SELECT * FROM DIRECTORS;


SELECT C.cID, C.cNAME, C.cHERO, C.cGENRE, C.cRELEASEDATE, D.dNAME, D.dEXPERIENCE
FROM CINEMA C
INNER JOIN DIRECTORS D 
ON C.cID = D.cID;

SELECT C.cID, C.cNAME, C.cHERO, C.cGENRE, C.cRELEASEDATE, D.dNAME, D.dEXPERIENCE
FROM CINEMA C
LEFT JOIN DIRECTORS D 
ON C.cID = D.cID;

SELECT C.cID , C.cNAME, D.dName 
FROM DIRECTORS D 
RIGHT JOIN CINEMA C 
ON C.cID = D.cID 
ORDER BY D.dNAME; 

SELECT C.cGENRE, D.dEXPERIENCE 
FROM CINEMA C 
FULL JOIN DIRECTORS D  
ON C.cID = D.cID 
ORDER BY C.cID;

SELECT C.*,D.* 
FROM CINEMA C 
CROSS JOIN DIRECTORS D;

SELECT C.*,D.* 
FROM DIRECTORS D
INNER JOIN CINEMA C 
ON C.cID = D.cID;


SELECT D.dNAME, COUNT(C.cID) AS MovieCount
FROM CINEMA C
INNER JOIN DIRECTORS D 
ON C.cID = D.cID
GROUP BY D.dNAME;

SELECT C.cGENRE, AVG(D.dEXPERIENCE) AS AvgExperience
FROM CINEMA C
LEFT JOIN DIRECTORS D 
ON C.cID = D.cID
GROUP BY C.cGENRE;

SELECT C.cGENRE, SUM(D.dEXPERIENCE) AS TotalExperience
FROM CINEMA C
LEFT JOIN DIRECTORS D 
ON C.cID = D.cID
GROUP BY C.cGENRE;

SELECT D.dName , COUNT(C.cID) AS TOTALMOVIES
FROM CINEMA C
INNER JOIN DIRECTORS D ON C.cID = D.cID
GROUP BY D.dNAME
HAVING SUM(D.dEXPERIENCE) > 10;


CREATE TABLE CCustomers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    City VARCHAR(50)
);
 
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10,2),
    FOREIGN KEY (CustomerID) REFERENCES CCustomers(CustomerID)
);
 
INSERT INTO CCustomers (CustomerID, CustomerName, City) VALUES
(1, 'Alice Johnson', 'New York'),
(2, 'Bob Smith', 'Los Angeles'),
(3, 'Charlie Brown', 'Chicago'),
(4, 'David Lee', 'Houston');
 
INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES
(101, 1, '2024-01-10', 500.00),
(102, 1, '2024-02-15', 1500.00),
(103, 2, '2024-01-20', 2000.00),
(104, 3, '2024-03-05', 3000.00),
(105, 4, '2024-03-10', 1200.00),
(106, 1, '2024-03-15', 700.00),
(107, 2, '2024-04-01', 1800.00),
(108, 3, '2024-04-05', 2500.00);
 
select * from Orders;
select * from CCustomers;
 
SELECT C.CustomerID, C.CustomerName, SUM(O.TotalAmount) AS TotalSpent
FROM CCustomers C
JOIN Orders O ON C.CustomerID = O.CustomerID
GROUP BY C.CustomerID, C.CustomerName;
 
 
SELECT C.CustomerID, C.CustomerName, SUM(O.TotalAmount) AS TotalSpent
FROM CCustomers C
JOIN Orders O ON C.CustomerID = O.CustomerID
GROUP BY C.CustomerID, C.CustomerName
HAVING SUM(O.TotalAmount) > 5000;
 
SELECT C.CustomerID, C.CustomerName, O.OrderDate, SUM(O.TotalAmount) AS TotalSpent
FROM CCustomers C
JOIN Orders O ON C.CustomerID = O.CustomerID
GROUP BY GROUPING SETS (
    (C.CustomerID, C.CustomerName), 
    (O.OrderDate),                   
    ()                               
);
 
 CREATE TABLE Clients (
    ClientID INT PRIMARY KEY,
    ClientName VARCHAR(100),
    Location VARCHAR(50)
);

CREATE TABLE Purchases (
    PurchaseID INT PRIMARY KEY,
    ClientID INT,
    PurchaseDate DATE,
    Amount DECIMAL(10,2),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);


INSERT INTO Clients (ClientID, ClientName, Location) VALUES
(1, 'Alice', 'New York'),
(2, 'Bob', 'Los Angeles'),
(3, 'Charlie', 'Chicago'),
(4, 'David', 'Houston'),
(5, 'Emma', 'San Francisco');


INSERT INTO Purchases (PurchaseID, ClientID, PurchaseDate, Amount) VALUES
(101, 1, '2024-03-01', 150.00),
(102, 1, '2024-03-05', 200.00),
(103, 2, '2024-03-02', 300.00),
(104, 3, '2024-03-04', 250.00),
(105, 3, '2024-03-10', 180.00),
(106, 4, '2024-03-06', 500.00),
(107, 4, '2024-03-08', 220.00),
(108, 5, '2024-03-11', 320.00);


SELECT P.PurchaseID, C.ClientID,C.ClientName FROM Purchases P 
JOIN Clients C ON C.ClientID = P.ClientID;

SELECT C.ClientID,C.ClientName,C.Location,P.PurchaseID,P.PurchaseDate,P.Amount 
FROM Clients C JOIN Purchases P ON C.ClientID = P.ClientID; 

SELECT C.ClientID, C.ClientName ,P.PurchaseDate
FROM Clients C JOIN Purchases P ON C.ClientID = P.ClientID
WHERE P.PurchaseDate BETWEEN '2024-03-01' AND '2024-03-31';

SELECT C.ClientID, C.ClientName, C.Location, P.PurchaseID, P.PurchaseDate, P.Amount
FROM Clients C
LEFT JOIN Purchases P ON C.ClientID = P.ClientID;

SELECT C.ClientID, C.ClientName, C.Location
FROM Clients C
LEFT JOIN Purchases P ON C.ClientID = P.ClientID
WHERE P.PurchaseID IS NULL;

SELECT C.ClientID, C.ClientName, P.PurchaseID, P.PurchaseDate, P.Amount
FROM Clients C
JOIN Purchases P ON C.ClientID = P.ClientID
WHERE P.PurchaseDate = '2024-03-06';

SELECT C.ClientID, C.ClientName, C.Location, P.PurchaseID, P.PurchaseDate, P.Amount
FROM Purchases P
RIGHT JOIN Clients C ON C.ClientID = P.ClientID;

SELECT C.ClientID, C.ClientName, C.Location, P.PurchaseID, P.PurchaseDate, P.Amount
FROM Clients C
FULL JOIN Purchases P ON C.ClientID = P.ClientID;

SELECT C.ClientID, C.ClientName, SUM(P.Amount) AS TotalSpent
FROM Clients C
JOIN Purchases P ON C.ClientID = P.ClientID
GROUP BY C.ClientID, C.ClientName;


SELECT ClientID, ClientName, Location 
FROM Clients 
WHERE ClientID IN (SELECT DISTINCT ClientID FROM Purchases);

SELECT C.ClientID, C.ClientName, C.Location
FROM Clients C
WHERE (SELECT SUM(P.Amount) FROM Purchases P WHERE P.ClientID = C.ClientID) > 500;



