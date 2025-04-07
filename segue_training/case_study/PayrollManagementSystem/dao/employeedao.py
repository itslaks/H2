import pyodbc
from entity.employee import Employee
from util.util import DBConnUtil


class EmployeeDAO:

    # Create
    def add_employee(self, employee):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Employee 
        (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(query, (employee.first_name, employee.last_name, employee.dob, employee.gender,
                               employee.email, employee.phone, employee.address, employee.position,
                               employee.joining_date, employee.termination_date))
        
        # Fetch the generated EmployeeID
        cursor.execute("SELECT SCOPE_IDENTITY()")
        employee_id = cursor.fetchone()[0]
        conn.commit()
        conn.close()
        return employee_id

    # Read (by ID)
    def get_employee_by_id(self, employee_id):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = "SELECT EmployeeID, FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate FROM Employee WHERE EmployeeID = ?"
        cursor.execute(query, (employee_id,))
        row = cursor.fetchone()
        conn.close()
        return Employee(*row) if row else None

    # Read (All)
    def get_all_employees(self):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = "SELECT EmployeeID, FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate, TerminationDate FROM Employee"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return [Employee(*row) for row in rows]

    # Update
    def update_employee(self, employee):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """UPDATE Employee SET FirstName=?, LastName=?, DateOfBirth=?, Gender=?, Email=?, PhoneNumber=?, Address=?, Position=?, JoiningDate=?, TerminationDate=? WHERE EmployeeID=?"""
        cursor.execute(query, (employee.first_name, employee.last_name, employee.dob, employee.gender,
                               employee.email, employee.phone, employee.address, employee.position,
                               employee.joining_date, employee.termination_date, employee.employee_id))
        conn.commit()
        conn.close()

    # Delete
    def delete_employee(self, employee_id):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM Employee WHERE EmployeeID = ?"
        cursor.execute(query, (employee_id,))
        conn.commit()
        conn.close()


# Sample Testing
if __name__ == "__main__":
    dao = EmployeeDAO()

    # Fetch All Employees
    employees = dao.get_all_employees()
    for emp in employees:
        print(f"{emp.employee_id}: {emp.first_name} {emp.last_name}")
