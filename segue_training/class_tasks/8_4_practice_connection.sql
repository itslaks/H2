create database studentmanagement;

create table student (
stuid int,
stuname VARCHAR(122),
studept VARCHAR(122),
stumarks int,
stuhome VARCHAR(122)
);


USE studentmanagement;
GO

SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'student';

select * from student;