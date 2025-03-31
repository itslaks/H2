CREATE DATABASE CarRentalSystem;

use CarRentalSystem;

CREATE TABLE Vehicle (
    VehicleID INT PRIMARY KEY,
    make VARCHAR(50),
    model VARCHAR(50),
    year INT,
    dailyRate DECIMAL(10,2),
    status VARCHAR(20),
    passengerCapacity INT,
    engineCapacity INT
);

CREATE TABLE Customer (
    customerID INT PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phoneNumber VARCHAR(20) UNIQUE
);

CREATE TABLE Lease (
    leaseID INT PRIMARY KEY,
    vehicleID INT FOREIGN KEY REFERENCES Vehicle(vehicleID) ON DELETE CASCADE,
    customerID INT FOREIGN KEY REFERENCES Customer(customerID) ON DELETE CASCADE,
    startDate DATE,
    endDate DATE,
    type VARCHAR(20)
);

CREATE TABLE Payment (
    paymentID INT PRIMARY KEY,
    leaseID INT FOREIGN KEY REFERENCES Lease(leaseID) ON DELETE CASCADE,
    paymentDate DATE,
    amount DECIMAL(10,2)
);



INSERT INTO Vehicle VALUES
(1, 'Toyota', 'Camry', 2022, 50.00, 'available', 4, 1450),
(2, 'Honda', 'Civic', 2023, 45.00, 'available', 7, 1500),
(3, 'Ford', 'Focus', 2022, 48.00, 'notAvailable', 4, 1400),
(4, 'Nissan', 'Altima', 2023, 52.00, 'available', 7, 1200),
(5, 'Chevrolet', 'Malibu', 2022, 47.00, 'available', 4, 1800),
(6, 'Hyundai', 'Sonata', 2023, 49.00, 'notAvailable', 7, 1400),
(7, 'BMW', '3 Series', 2023, 60.00, 'available', 7, 2499),
(8, 'Mercedes', 'C-Class', 2022, 58.00, 'available', 8, 2599),
(9, 'Audi', 'A4', 2022, 55.00, 'notAvailable', 4, 2500),
(10, 'Lexus', 'ES', 2023, 54.00, 'available', 4, 2500);

SELECT * FROM Vehicle;



INSERT INTO Customer VALUES
(1, 'John', 'Doe', 'johndoe@example.com', '555-555-5555'),
(2, 'Jane', 'Smith', 'janesmith@example.com', '555-123-4567'),
(3, 'Robert', 'Johnson', 'robert@example.com', '555-789-1234'),
(4, 'Sarah', 'Brown', 'sarah@example.com', '555-456-7890'),
(5, 'David', 'Lee', 'david@example.com', '555-987-6543'),
(6, 'Laura', 'Hall', 'laura@example.com', '555-234-5678'),
(7, 'Michael', 'Davis', 'michael@example.com', '555-876-5432'),
(8, 'Emma', 'Wilson', 'emma@example.com', '555-432-1098'),
(9, 'William', 'Taylor', 'william@example.com', '555-321-6547'),
(10, 'Olivia', 'Adams', 'olivia@example.com', '555-765-4321');

SELECT * FROM Customer;


INSERT INTO Lease VALUES
(1, 1, 1, '2023-01-01', '2023-01-05', 'Daily'),
(2, 2, 2, '2023-02-15', '2023-02-28', 'Monthly'),
(3, 3, 3, '2023-03-10', '2023-03-15', 'Daily'),
(4, 4, 4, '2023-04-20', '2023-04-30', 'Monthly'),
(5, 5, 5, '2023-05-05', '2023-05-10', 'Daily'),
(6, 4, 3, '2023-06-15', '2023-06-30', 'Monthly'),
(7, 7, 7, '2023-07-01', '2023-07-10', 'Daily'),
(8, 8, 8, '2023-08-12', '2023-08-15', 'Monthly'),
(9, 3, 3, '2023-09-07', '2023-09-10', 'Daily'),
(10, 10, 10, '2023-10-10', '2023-10-31', 'Monthly');

SELECT * FROM Lease;


INSERT INTO Payment VALUES
(1, 1, '2023-01-03', 200.00),
(2, 2, '2023-02-20', 1000.00),
(3, 3, '2023-03-12', 75.00),
(4, 4, '2023-04-25', 900.00),
(5, 5, '2023-05-07', 60.00),
(6, 6, '2023-06-18', 1200.00),
(7, 7, '2023-07-03', 40.00),
(8, 8, '2023-08-14', 1100.00),
(9, 9, '2023-09-09', 80.00),
(10, 10, '2023-10-25', 1500.00);

SELECT * FROM Payment;



--1. Update the daily rate for a Mercedes car to 68.
UPDATE Vehicle SET dailyRate = 68.00
WHERE make = 'Mercedes';

SELECT * FROM Vehicle WHERE make = 'Mercedes';


--2. Delete a specific customer and all associated leases and payments.
DELETE FROM Customer WHERE customerID = 3;

SELECT * FROM Customer;


--3.Rename the "paymentDate" column in the Payment table to "transactionDate".
EXEC sp_rename 'Payment.paymentDate', 'transactionDate', 'COLUMN';


--4. Find a specific customer by email.SELECT * FROM Customer WHERE email = 'sarah@example.com';


--5. Get active leases for a specific customer.INSERT INTO Vehicle VALUES
(11, 'Tesla', 'Model S', 2025, 80.00, 'available', 5, 0),
(12, 'Ford', 'Mustang', 2025, 75.00, 'available', 4, 5000),
(13, 'Chevrolet', 'Corvette', 2025, 85.00, 'available', 2, 6200);

INSERT INTO Customer VALUES
(11, 'Ram', 'Kumar', 'ram@example.com', '123-456-7890'),
(12, 'Harish', 'S', 'harishs@example.com', '103-456-7410'),
(13, 'Ryan', 'Miller', 'ryan.miller@example.com', '789-456-1230');

INSERT INTO Lease VALUES
(11, 11, 11, '2025-03-01', '2025-04-01', 'Monthly'),  
(12, 12, 12, '2025-03-15', '2025-05-15', 'Monthly'),  
(13, 13, 13, '2025-04-01', '2025-06-01', 'Monthly');  

INSERT INTO Payment VALUES
(11, 11, '2025-03-05', 2400.00), 
(12, 12, '2025-03-20', 3000.00), 
(13, 13, '2025-04-05', 2550.00); 

SELECT * FROM Lease WHERE customerID = 11 AND 
GETDATE() BETWEEN startDate AND endDate;



-- 6.Find all payments made by a customer with a specific phone number.
select p.* from Payment p
INNER JOIN Lease l ON p.leaseID = l.leaseID
INNER JOIN Customer c ON l.customerID = c.customerID
where c.phoneNumber = '555-456-7890';


--7. Calculate the average daily rate of all available cars.
SELECT AVG(dailyRate) AS AverageDailyRate
FROM Vehicle
WHERE status = 'available';


--8. Find the car with the highest daily rate.
SELECT TOP 1 * FROM Vehicle ORDER BY dailyRate DESC;


--9. Retrieve all cars leased by a specific customer.
SELECT V.* FROM Vehicle V
JOIN Lease L ON V.vehicleID = L.vehicleID
WHERE L.customerID = 12;


--10. Find the details of the most recent lease.
SELECT TOP 1 * FROM Lease ORDER BY endDate DESC;


--11. List all payments made in the year 2023.
SELECT * FROM Payment WHERE YEAR(transactionDate) = 2023;


--12. Retrieve customers who have not made any payments. 
SELECT c.*
FROM Customer c
LEFT JOIN Lease l ON c.customerID = l.customerID
LEFT JOIN Payment p ON l.leaseID = p.leaseID
WHERE p.paymentID IS NULL;


--13.Retrieve Car Details and Their Total Payments.SELECT V.vehicleID, V.make, V.model, SUM(P.amount) AS TotalPayment
FROM Vehicle V
JOIN Lease L ON V.vehicleID = L.vehicleID
JOIN Payment P ON L.leaseID = P.leaseID
GROUP BY V.vehicleID, V.make, V.model;


--14.Calculate Total Payments for Each Customer.
SELECT C.customerID, C.firstName, C.lastName, SUM(P.amount) AS totalPayments
FROM Customer C
JOIN Lease L ON C.customerID = L.customerID
JOIN Payment P ON L.leaseID = P.leaseID
GROUP BY C.customerID, C.firstName, C.lastName;


--15. List Car Details for Each Lease.
SELECT L.leaseID, C.firstName, C.lastName, V.make, V.model, L.startDate, L.endDate
FROM Lease L
JOIN Customer C ON L.customerID = C.customerID
JOIN Vehicle V ON L.vehicleID = V.vehicleID;


--16. Retrieve Details of Active Leases with Customer and Car Information.
SELECT L.leaseID, C.firstName, C.lastName, V.make, V.model, L.startDate, L.endDate
FROM Lease L
JOIN Customer C ON L.customerID = C.customerID
JOIN Vehicle V ON L.vehicleID = V.vehicleID
WHERE GETDATE() BETWEEN l.startDate AND l.endDate;


--17. Find the Customer Who Has Spent the Most on Leases
SELECT TOP 1 C.customerID, C.firstName, C.lastName, SUM(P.amount) AS totalSpent
FROM Customer C
JOIN Lease L ON C.customerID = L.customerID
JOIN Payment P ON L.leaseID = P.leaseID
GROUP BY C.customerID, C.firstName, C.lastName
ORDER BY totalSpent DESC;


--18.List All Cars with Their Current Lease Information
SELECT V.vehicleID, V.make, V.model, 
       L.leaseID, L.startDate, L.endDate, L.type
FROM Vehicle V
LEFT JOIN Lease L ON V.vehicleID = L.vehicleID
ORDER BY V.vehicleID;





















