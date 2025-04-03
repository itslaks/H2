num_students = int(input("Enter the number of students: "))

for i in range(1, num_students + 1):
    while True:
        try:
            score = int(input(f"Enter score for student {i} (0-100): "))
            if 0 <= score <= 100:
                break  
            else:
                print("Please enter a valid score between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")

   
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Student {i} Grade: {grade}\n")

