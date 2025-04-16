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



