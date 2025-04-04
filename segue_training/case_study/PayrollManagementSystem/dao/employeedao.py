import pyodbc
from entity.employee import Employee
from util.util import DBConnUtil


class EmployeeDAO:
    def add_employee(self, employee):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Employee (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(query, (employee.first_name, employee.last_name, employee.dob, employee.gender,
                               employee.email, employee.phone, employee.address, employee.position,
                               employee.joining_date, employee.termination_date))
        conn.commit()
        conn.close()

    def get_employee_by_id(self, employee_id):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Employee WHERE EmployeeID = ?"
        cursor.execute(query, (employee_id,))
        row = cursor.fetchone()
        conn.close()
        return Employee(*row) if row else None
    


dao = EmployeeDAO()
employee = dao.get_employee_by_id(1)
if employee:
    print(f"Employee Found: {employee.first_name} {employee.last_name}")
else:
    print("Employee not found.")

