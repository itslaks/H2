Create Database HospitalManagementSystem;
use HospitalManagementSystem;


CREATE TABLE Patient (
    patientId INT PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    dateOfBirth DATE,
    gender VARCHAR(10),
    contactNumber VARCHAR(15),
    address VARCHAR(255)
);

CREATE TABLE Doctor (
    doctorId INT PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    specialization VARCHAR(100),
    contactNumber VARCHAR(15)
);

CREATE TABLE Appointment (
    appointmentId INT PRIMARY KEY,
    patientId INT,
    doctorId INT,
    appointmentDate DATETIME,
    description VARCHAR(255),
    FOREIGN KEY (patientId) REFERENCES Patient(patientId) ON DELETE CASCADE,
    FOREIGN KEY (doctorId) REFERENCES Doctor(doctorId) ON DELETE CASCADE
);


INSERT INTO Patient VALUES
(1, 'Amit', 'Sharma', '1990-05-12', 'Male', '9876543210', 'Delhi'),
(2, 'Sneha', 'Patil', '1988-03-15', 'Female', '9123456780', 'Mumbai'),
(3, 'Raj', 'Kumar', '1992-07-20', 'Male', '9876504321', 'Chennai'),
(4, 'Pooja', 'Rao', '1995-11-02', 'Female', '9001234567', 'Bengaluru'),
(5, 'Arjun', 'Mehta', '1985-04-10', 'Male', '9812345678', 'Ahmedabad'),
(6, 'Kavita', 'Singh', '1993-09-25', 'Female', '9988776655', 'Kolkata'),
(7, 'Ravi', 'Joshi', '1991-01-30', 'Male', '9765432109', 'Pune'),
(8, 'Neha', 'Desai', '1994-08-14', 'Female', '9678901234', 'Surat'),
(9, 'Manish', 'Verma', '1989-06-18', 'Male', '9898989898', 'Jaipur'),
(10, 'Anjali', 'Kapoor', '1996-12-05', 'Female', '9555123456', 'Hyderabad');



INSERT INTO Doctor VALUES
(101, 'Dr. Ramesh', 'Gupta', 'Cardiology', '9012345678'),
(102, 'Dr. Seema', 'Reddy', 'Neurology', '9023456789'),
(103, 'Dr. Arvind', 'Patel', 'Orthopedics', '9034567890'),
(104, 'Dr. Leela', 'Nair', 'Pediatrics', '9045678901'),
(105, 'Dr. Vikram', 'Malhotra', 'Dermatology', '9056789012'),
(106, 'Dr. Meera', 'Iyer', 'Gynecology', '9067890123'),
(107, 'Dr. Sunil', 'Bansal', 'ENT', '9078901234'),
(108, 'Dr. Divya', 'Joshi', 'Oncology', '9089012345'),
(109, 'Dr. Harish', 'Mishra', 'General Medicine', '9090123456'),
(110, 'Dr. Priya', 'Kohli', 'Psychiatry', '9101234567');



INSERT INTO Appointment VALUES
(1001, 1, 101, '2025-04-01', 'Routine checkup'),
(1002, 2, 102, '2025-04-02', 'Headache consultation'),
(1003, 3, 103, '2025-04-03', 'Knee pain'),
(1004, 4, 104, '2025-04-04', 'Child fever'),
(1005, 5, 105, '2025-04-05', 'Skin rash'),
(1006, 6, 106, '2025-04-06', 'Pregnancy follow-up'),
(1007, 7, 107, '2025-04-07', 'Ear pain'),
(1008, 8, 108, '2025-04-08', 'Cancer screening'),
(1009, 9, 109, '2025-04-09', 'General checkup'),
(1010, 10, 110, '2025-04-10', 'Anxiety issue');





SELECT * FROM Appointment;


CREATE TABLE NewRecords (
    RecordId INT PRIMARY KEY,
    RecordType VARCHAR(230),
    doctorId INT,
    appointmentDate DATETIME
);

