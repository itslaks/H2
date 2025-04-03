# 1) Write a Python program that takes an integer input from the user and prints "Positive" if the number is greater than 0.

num = int(input("Enter a number: "))
if num > 0:
    print("Positive")

 
# 2) Given a variable temperature, write an if statement that prints "Hot day!" if temperature is greater than 30.

temperature = float(input("Enter temperature: "))
if temperature > 30:
    print("Hot day!")

 
# 3) Write a program that asks the user to enter a number and checks if it is even. If it is, print "Even number".

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")

 
# 4) Write a Python program that checks if a number is even or odd. Print "Even" if it is even, otherwise print "Odd".

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

 
# 5)Write a program that asks the user to enter their age. If they are 18 or older, print "Eligible to vote", otherwise print "Not eligible to vote".

age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

 
# 6)Create a program that asks the user to enter a password. If the password is "admin123", print "Access Granted", otherwise print "Access Denied".

password = input("Enter password: ")
if password == "admin123":
    print("Access Granted")
else:
    print("Access Denied")

 
# 7)Write a program that takes a number as input and prints:
 
# "Positive" if the number is greater than 0,
 
# "Negative" if it is less than 0,
 
# "Zero" if it is exactly 0.

num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

 
# 8)Create a grading system where a user enters a score (0-100). The program should print:
 
# "A" if the score is 90 or above,
 
# "B" if the score is between 80 and 89,
 
# "C" if the score is between 70 and 79,
 
# "D" if the score is between 60 and 69,
 
# "F" if the score is below 60.

score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

 
# 9)Write a Python program that checks if a given year is a leap year. A leap year:
 
# Is divisible by 400, or
 
# Is divisible by 4 but not by 100.

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

 
# 10)Write a Python program that takes the current time (in 24-hour format) as input and prints:
 
# "Good Morning" if the time is between 5 and 12,
 
# "Good Afternoon" if the time is between 12 and 17,
 
# "Good Evening" if the time is between 17 and 21,
 
# "Good Night" otherwise.

time = int(input("Enter the current time (0-23): "))

if 5 <= time < 12:
    print("Good Morning")
elif 12 <= time < 17:
    print("Good Afternoon")
elif 17 <= time < 21:
    print("Good Evening")
else:
    print("Good Night")
