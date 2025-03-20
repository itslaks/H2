CREATE TABLE Customers (
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    Email NVARCHAR(100) UNIQUE NOT NULL,
    Phone NVARCHAR(15) NOT NULL,
    Address NVARCHAR(255) NOT NULL
);

SELECT * FROM Customers;

CREATE TABLE Products (
    ProductID INT IDENTITY(1,1) PRIMARY KEY,
    ProductName NVARCHAR(100) NOT NULL,
    Description NVARCHAR(255),
    Price DECIMAL(10,2) CHECK (Price > 0) NOT NULL
);

SELECT * FROM Products;


CREATE TABLE Orders (
    OrderID INT IDENTITY(1,1) PRIMARY KEY,
    CustomerID INT NOT NULL,
    OrderDate DATETIME DEFAULT GETDATE(),
    TotalAmount DECIMAL(10,2) CHECK (TotalAmount >= 0),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);


SELECT * FROM Orders;

CREATE TABLE OrderDetails (
    OrderDetailID INT IDENTITY(1,1) PRIMARY KEY,
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT CHECK (Quantity > 0) NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

SELECT * FROM OrderDetails;


CREATE TABLE Inventory (
    InventoryID INT IDENTITY(1,1) PRIMARY KEY,
    ProductID INT NOT NULL UNIQUE,
    QuantityInStock INT CHECK (QuantityInStock >= 0) NOT NULL,
    LastStockUpdate DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);


SELECT * FROM Inventory;


INSERT INTO Customers VALUES
('Ram', 'Verma', 'ramverma@yahoo.com', '9876543210', '12 MG Road, Delhi'),
('Kishore', 'Patel', 'kishorepatel@gmail.com', '8765432109', '34 Park Street, Mumbai'),
('Kumar', 'Reddy', 'kumarreddy@yahoo.com', '7654321098', '56 Brigade Road, Bangalore'),
('Haley', 'Pearl', 'haleypearl@gmail.com', '6543210987', '78 Connaught Place, Delhi'),
('Nan', 'laks', 'nan.laks@yahoo.com', '5432109876', '90 Banjara Hills, Hyderabad'),
('Harish', 'potta', 'harish@outlook.com', '4321098765', '21 Sarojini Nagar, Chennai'),
('Kamalesh', 'waran', 'kamalesh@yahoo.com', '3210987654', '33 MG Road, Pune'),
('Rahul', 'logesh', 'delhi@gmail.com', '2109876543', '45 Koramangala, Bangalore'),
('Virat', 'kohli', 'anushka@rcb.com', '1098765432', '67 Jubilee Hills, Hyderabad'),
('joshy', 'agarwal', 'joshy@outlook.com', '9988776655', '89 Indiranagar, Bangalore');

SELECT * FROM Customers;




INSERT INTO Products (ProductName, Description, Price) VALUES
('Laptop', 'HP PAVILION EC 2004 AX', 58000),
('Smartphone', 'REALME GT NEO 3T', 32000),
('Tablet', 'Apple iPad Pro 12.9-inch', 90000),
('Smartwatch', 'BOAT IZTRA', 4500),
('Headphones', 'CMF BUDS PRO', 3000),
('Camera', 'Canon EOS 90D DSLR Camera', 120000),
('Gaming Console', 'Sony PlayStation 5', 50000),
('Monitor', 'LG 4K UltraFine 27-inch Monitor', 40000),
('Keyboard', 'Logitech MX Keys Wireless Keyboard', 12000),
('Mouse', 'Razer DeathAdder V2 Gaming Mouse', 5000);

SELECT * FROM Products;




INSERT INTO Inventory (ProductID, QuantityInStock) VALUES
(1, 20),
(2, 30),
(3, 15),
(4, 25),
(5, 40),
(6, 10),
(7, 12),
(8, 18),
(9, 50),
(10, 35);

SELECT * FROM Inventory;



INSERT INTO Orders (CustomerID, TotalAmount) VALUES
(1, 240000),
(2, 85000),
(3, 90000),
(4, 45000),
(5, 30000),
(6, 120000),
(7, 50000),
(8, 40000),
(9, 12000),
(10, 5000);


SELECT * FROM Orders;


INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES
(1, 1, 2),
(2, 2, 1),
(3, 3, 1),
(4, 4, 2),
(5, 5, 3),
(6, 6, 1),
(7, 7, 1),
(8, 8, 2),
(9, 9, 1),
(10, 10, 2);

SELECT * FROM OrderDetails;


SELECT FirstName, LastName, Email 
FROM Customers;


SELECT O.OrderID, O.OrderDate, C.FirstName, C.LastName 
FROM Orders O
JOIN Customers C ON O.CustomerID = C.CustomerID;



INSERT INTO Customers VALUES 
('king', 'kong', 'kkang@jungle.com', '9876543211', 'vandoolur, Chennai');

SELECT * FROM Customers WHERE FirstName = 'king';

SELECT * FROM Customers;


UPDATE Products SET Price = Price * 1.10;
SELECT Price FROM Products; 




DELETE FROM OrderDetails WHERE OrderID = 2;
SELECT * FROM Orders;

DELETE FROM Orders WHERE OrderID = 2;
SELECT * FROM OrderDetails;




INSERT INTO Orders (CustomerID, OrderDate, TotalAmount) 
VALUES (2,2024-12-20, 75000);
SELECT * FROM Orders;




UPDATE Customers SET Email = 'jacksparrow@xbox.com', Address = 'middle of ocean Atlanta' WHERE CustomerID = 3;
SELECT * FROM Customers;



UPDATE Orders 
SET TotalAmount = (
    SELECT SUM(P.Price * OD.Quantity) 
    FROM OrderDetails OD 
    JOIN Products P ON OD.ProductID = P.ProductID 
    WHERE OD.OrderID = Orders.OrderID
);

SELECT * FROM Orders;


DELETE FROM OrderDetails WHERE OrderID IN (SELECT OrderID FROM Orders WHERE CustomerID = 5);
DELETE FROM Orders WHERE CustomerID = 5;
SELECT * FROM Orders;



INSERT INTO Products (ProductName, Description, Price) 
VALUES ('AR GLASS', 'META GLASSES', 15000000);
SELECT * FROM Products;




ALTER TABLE Orders ADD OrderStatus NVARCHAR(20) DEFAULT 'Pending';
UPDATE Orders SET OrderStatus = @NewStatus WHERE OrderID = @OrderID;

SELECT * FROM Orders;




ALTER TABLE Customers ADD OrderCount INT DEFAULT 0;

UPDATE Customers 
SET OrderCount = (
    SELECT COUNT(*) 
    FROM Orders 
    WHERE Orders.CustomerID = Customers.CustomerID
);

SELECT * FROM Customers;