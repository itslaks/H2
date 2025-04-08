import pyodbc
 
server = r'HP_PAVILION\SQLEXPRESS01'
database = 'studentmanagement'
driver = '{ODBC Driver 17 for SQL Server}'
 
conn = pyodbc.connect(
    f'DRIVER={driver};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f"Trusted_Connection=yes;"
)
 
cursor = conn.cursor()


def create_student(stuid, stuname, studept, stumarks, stuhome):
    cursor.execute("INSERT INTO student (stuId, stuName, stuDept, stuMarks, stuHome) VALUES (?,?,?,?,?)",
                   (stuid, stuname, studept, stumarks, stuhome))
    conn.commit()


def read_student():
    cursor.execute("SELECT * FROM student")
    for row in cursor.fetchall():
        print(row)


def update_student(stuid):
    print("Which field do you want to update?")
    print("1. Name")
    print("2. Department")
    print("3. Marks")
    print("4. Home Town")

    choice = int(input("Enter choice (1-4): "))

    if choice == 1:
        new_value = input("Enter new Name: ")
        cursor.execute("UPDATE student SET stuName=? WHERE stuId=?", (new_value, stuid))

    elif choice == 2:
        new_value = input("Enter new Department: ")
        cursor.execute("UPDATE student SET stuDept=? WHERE stuId=?", (new_value, stuid))

    elif choice == 3:
        new_value = input("Enter new Marks: ")
        cursor.execute("UPDATE student SET stuMarks=? WHERE stuId=?", (new_value, stuid))

    elif choice == 4:
        new_value = input("Enter new Home Town: ")
        cursor.execute("UPDATE student SET stuHome=? WHERE stuId=?", (new_value, stuid))

    else:
        print("Invalid Choice!")

    conn.commit()
    print("Student Details Updated Successfully!")


def delete_student(stuid):
    cursor.execute("DELETE FROM student WHERE stuId=?", (stuid,))
    conn.commit()
    print("Student Deleted!!")


# Function Calls
create_student(1, 'Laks', 'AI', '88', 'KGM')
create_student(2, 'Haley', 'AI', '88', 'MDR')

print("Before Update:")
read_student()

update_student(1)  

print("After Update:")
read_student()

delete_student(2)

print("After Delete:")
read_student()
