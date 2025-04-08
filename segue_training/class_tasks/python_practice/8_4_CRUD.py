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

def create_student(stuid,stuname,studept,stumarks,stuhome):
    cursor.execute("INSERT INTO student (stuId, stuName, stuDept, stuMarks, stuHome) values (?,?,?,?,?)",
               (stuid, stuname, studept, stumarks, stuhome))

    conn.commit()

create_student(1, 'Laks', 'AI', '88', 'KGM')


def read_student():
    cursor.execute("SELECT * FROM student")
    for row in cursor .fetchall():
        print(row)


def update_student(stuid,stuhome):
    cursor.execute(
        "UPDATE student SET stuhome=? WHERE stuid =?",(stuid,stuhome)
    )
    conn.commit()
    print("Details of student has been Updated")
 
 
def delete_student(stuid):
    cursor.execute("DELETE FROM student WHERE stuid=?",(stuid))
    conn.commit()
    print("Student Deleted!!")


create_student(2, 'Haley', 'AI', '88', 'MDR')
read_student()
delete_student(2)
read_student()