SELECT O.OrderID, C.FirstName, C.LastName, O.OrderDate, O.TotalAmount
FROM Orders O
JOIN Customers C ON O.CustomerID = C.CustomerID;

SELECT ProductName , Price FROM Products;

SELECT ProductName , SUM(Price) AS TotalRevenue FROM Products GROUP BY ROLLUP (ProductName);


