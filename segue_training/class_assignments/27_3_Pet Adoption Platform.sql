CREATE DATABASE PETCARE;

use PETCARE;

CREATE TABLE Pets (
PetID INT NOT NULL PRIMARY KEY IDENTITY (1,1),
Name VARCHAR(55),
Age INT,
Breed VARCHAR(55),
Type VARCHAR(55),
AvailableForAdoption NVARCHAR(50) CHECK (AvailableForAdoption IN ('Yes','No'))
);

CREATE TABLE Shelters (
ShelterID INT IDENTITY(1,1) ,
Name VARCHAR(50),
Location VARCHAR(75)
);

CREATE TABLE Donations (
DonationID INT IDENTITY(1,1),
DonorName VARCHAR(55),
DonationType VARCHAR(55),
DonationAmount INT,
DonationItem VARCHAR(55),
DonationDate DATETIME
);

CREATE TABLE AdoptionEvents (
EventID INT NOT NULL PRIMARY KEY,
EventName VARCHAR(55),
EventDate DATETIME,
Location VARCHAR(55)
);

CREATE TABLE Participants (
ParticipantID INT IDENTITY(1,1),
ParticipantName VARCHAR(55),
ParticipantType VARCHAR(55),
EventID INT FOREIGN KEY REFERENCES AdoptionEvents(EventID) ON DELETE CASCADE
);


INSERT INTO Pets (Name, Age, Breed, Type, AvailableForAdoption) VALUES
('Buddy', 2, 'Golden Retriever', 'Dog', 'Yes'),
('Mittens', 3, 'Persian', 'Cat', 'Yes'),
('Charlie', 1, 'Labrador', 'Dog', 'Yes'),
('Luna', 4, 'Siberian', 'Cat', 'No'),
('Rocky', 6, 'Bulldog', 'Dog', 'Yes'),
('Shadow', 2, 'German Shepherd', 'Dog', 'Yes');


INSERT INTO Shelters (Name, Location) VALUES
('Happy Paws', 'New York'),
('Safe Haven', 'Los Angeles'),
('Rescue Home', 'Chicago'),
('Pet Paradise', 'Houston'),
('Furry Friends', 'Miami'),
('Animal Haven', 'Seattle');


INSERT INTO Donations (DonorName, DonationType, DonationAmount, DonationItem, DonationDate) VALUES
('John Doe', 'Cash', 200.00, NULL, '2025-03-15'),
('Emma Smith', 'Food', 0, 'Dog Food', '2025-03-16'),
('Liam Johnson', 'Cash', 150.00, NULL, '2025-03-17'),
('Sophia Brown', 'Medicine', 0, 'Vet Supplies', '2025-03-18'),
('Mason White', 'Cash', 300.00, NULL, '2025-03-19'),
('Olivia Green', 'Blankets', 0, 'Pet Blankets', '2025-03-20');


INSERT INTO AdoptionEvents (EventID, EventName, EventDate, Location) VALUES
(1, 'Spring Adoption Fair', '2025-04-01', 'New York'),
(2, 'Summer Pet Meet', '2025-05-15', 'Los Angeles'),
(3, 'Rescue Awareness Day', '2025-06-10', 'Chicago'),
(4, 'Pet Care Expo', '2025-07-20', 'Houston'),
(5, 'Adopt a Friend', '2025-08-05', 'Miami'),
(6, 'Paws & Claws Festival', '2025-09-12', 'Seattle');


INSERT INTO Participants (ParticipantName, ParticipantType, EventID) VALUES
('Michael Johnson', 'Volunteer', 1),
('Sarah Lee', 'Adopter', 2),
('David Kim', 'Donor', 3),
('Emily White', 'Vet', 4),
('Kevin Brown', 'Trainer', 5),
('Sophia Miller', 'Shelter Rep', 6);


-- 3) Retrieve Available Pets
SELECT Name, Age, Breed, Type, AvailableForAdoption FROM Pets ORDER BY Age;

-- 4) SQL query to list participant names and types for a specific event based on EventID.
DECLARE @EventID INT = 1;
SELECT ParticipantName, ParticipantType 
FROM Participants 
WHERE EventID = @EventID;

-- 5)stored procedure to update a shelter’s name and location
CREATE PROCEDURE UpdateShelterInfo
@ShelterID INT,@NewName NVARCHAR(100),@NewLocation NVARCHAR(100)
AS BEGIN
UPDATE Shelters 
SET Name = @NewName, Location = @NewLocation WHERE ShelterID = @ShelterID;
END;

EXEC UpdateShelterInfo 2, 'Simba', 'Amazon forests';

SELECT * FROM Shelters;


--6) SQL query to calculate the total donation amount per shelter
SELECT s.Name AS ShelterName, SUM(d.DonationAmount) AS TotalDonations
FROM Shelters s
JOIN Donations d ON s.ShelterID = d.DonationID
GROUP BY s.Name;

--7) SQL query to list all pets that do not have an owner.
SELECT * FROM Pets WHERE AvailableForAdoption = 'Yes' ORDER BY Age;

-- 8) SQL query to retrieve total donations per month and year
SELECT YEAR(DonationDate) AS Year, MONTH(DonationDate) AS Month, SUM(DonationAmount) AS TotalDonations
FROM Donations
GROUP BY YEAR(DonationDate), MONTH(DonationDate);

-- 9) Retrieve distinct pet breeds where pets are aged between 1 and 3 years or older than 5 years
SELECT Name, Breed, Age FROM Pets WHERE Age BETWEEN 1 AND 3 OR Age > 5 
ORDER BY Age;

-- 10) List all pets and their respective shelters where pets are available for adoption
SELECT P.Name, P.AvailableForAdoption, S.Name, S.Location FROM Pets P
JOIN Shelters S ON S.ShelterID = P.PetID WHERE P.AvailableForAdoption = 'Yes';

--11)Count Event Participants by City:
DECLARE @City NVARCHAR(100) = 'New York';
SELECT COUNT(*) AS TotalParticipants
FROM AdoptionEvents e
JOIN Participants p ON e.EventID = p.EventID
WHERE e.Location = @City;

--12) Unique Breeds of Young Pets:
SELECT DISTINCT Breed FROM Pets WHERE Age BETWEEN 1 AND 5;

--13. Find Pets Not Yet Adopted:
SELECT * FROM Pets WHERE AvailableForAdoption = 1;

--14. Retrieve Adopted Pets and Adopters:
SELECT p.Name AS PetName, pa.ParticipantName AS Adopter
FROM Pets p
JOIN Participants pa ON p.PetID = pa.ParticipantID;

--15.  Count Available Pets in Shelters
SELECT s.Name AS ShelterName, COUNT(p.PetID) AS AvailablePets
FROM Shelters s
LEFT JOIN Pets p ON s.ShelterID = p.PetID
WHERE p.AvailableForAdoption = 'Yes'
GROUP BY s.Name;



--16. Find Matching Pet Pairs in Shelters:
SELECT p1.Name AS Pet1, p2.Name AS Pet2, p1.Breed, s.Name AS Shelter
FROM Pets p1
JOIN Pets p2 ON p1.PetID = p2.PetID AND p1.Breed = p2.Breed AND p1.PetID < p2.PetID
JOIN Shelters s ON p1.PetID = s.ShelterID;


--17. Find All Shelter-Event Combinations
SELECT s.Name AS Shelter, e.EventName AS Event
FROM Shelters s
CROSS JOIN AdoptionEvents e;

--18.Identify the Most Successful Shelter
SELECT s.Name AS Shelter_Name, COUNT(*) AS Total_Adoptions
FROM Shelters s
JOIN Pets p ON s.ShelterID = p.PetID
WHERE p.AvailableForAdoption = 'No'
GROUP BY s.Name
ORDER BY Total_Adoptions DESC;



--19. Trigger for Adoption Status Update
CREATE OR ALTER TRIGGER UpdateAdoptionStatus 
ON Participants
AFTER INSERT 
AS 
BEGIN
    SET NOCOUNT ON;
    
    -- Update only existing pets and ensure only adoptable pets are updated
    UPDATE Pets
    SET AvailableForAdoption = 0
    WHERE PetID IN (SELECT PetID FROM inserted)
    AND AvailableForAdoption = 1; 
END;


-- 20. Data Integrity Check: Prevent Duplicate Adoptions
-- Check if the constraint exists before adding it
IF NOT EXISTS (
    SELECT 1 FROM sys.objects 
    WHERE type = 'UQ' AND name = 'UniqueAdoption'
)
BEGIN
    ALTER TABLE Participants 
    ADD CONSTRAINT UniqueAdoption UNIQUE (ParticipantName, EventID);
END;






