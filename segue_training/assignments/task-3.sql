use TechShop;

-- Retrieve a list of all orders along with customer information (e.g., customer name) for each order.
SELECT O.OrderID, O.OrderDate, C.FirstName, C.LastName, O.TotalAmount
FROM Orders O
JOIN Customers C ON O.CustomerID = C.CustomerID;

--Find the total revenue generated by each electronic gadget product.
SELECT P.ProductName, SUM(OD.Quantity * P.Price) AS TotalRevenue
FROM OrderDetails OD
JOIN Products P ON OD.ProductID = P.ProductID
GROUP BY P.ProductName;

--List all customers who have made at least one purchase, including their names and contact information.
SELECT DISTINCT C.CustomerID, C.FirstName, C.LastName, C.Email, C.Phone
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID;

--Find the most popular electronic gadget (highest total quantity ordered).
SELECT TOP 1 P.ProductName, SUM(OD.Quantity) AS TotalQuantityOrdered
FROM OrderDetails OD
JOIN Products P ON OD.ProductID = P.ProductID
GROUP BY P.ProductName
ORDER BY TotalQuantityOrdered DESC;

--Retrieve a list of electronic gadgets along with their corresponding categories.
SELECT ProductID, ProductName, Description
FROM Products;

--Calculate the average order value for each customer.
SELECT C.CustomerID, C.FirstName, C.LastName, AVG(O.TotalAmount) AS AvgOrderValue
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID
GROUP BY C.CustomerID, C.FirstName, C.LastName;

--Find the order with the highest total revenue.
SELECT TOP 1 O.OrderID, C.FirstName, C.LastName, O.TotalAmount
FROM Orders O
JOIN Customers C ON O.CustomerID = C.CustomerID
ORDER BY O.TotalAmount DESC;

--List electronic gadgets and the number of times each product has been ordered.
SELECT P.ProductName, COUNT(OD.OrderDetailID) AS TimesOrdered
FROM OrderDetails OD
JOIN Products P ON OD.ProductID = P.ProductID
GROUP BY P.ProductName
ORDER BY TimesOrdered DESC;

--Find customers who have purchased a specific electronic gadget.
SELECT DISTINCT C.CustomerID, C.FirstName, C.LastName, C.Email
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID
JOIN OrderDetails OD ON O.OrderID = OD.OrderID
JOIN Products P ON OD.ProductID = P.ProductID
WHERE P.ProductName = 'LAPTOP';  

--Calculate the total revenue generated by all orders placed within a specific time period.
SELECT SUM(TotalAmount) AS TotalRevenue
FROM Orders
WHERE OrderDate BETWEEN '2025-03-01' AND '2025-10-29'; 







