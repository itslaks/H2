create database myproject;
 
use myproject;
 
create table Quiz_Questions(

id int primary key identity(1,1),

question varchar(255),

option_a varchar(100),

option_b varchar(100),

option_c varchar(100),

option_d varchar(100),

correct_option char(1)

);
 
 
create table Player_Score(

id int primary key identity(1,1),

player_name varchar(100),

score int

);
 
create table Execution_Logs(

	id int primary key identity(1,1),

	event_description varchar(255),

	timestamp datetime

);
 

 SELECT * FROM Player_Score;