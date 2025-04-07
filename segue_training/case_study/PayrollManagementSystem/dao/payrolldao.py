import pyodbc
from entity.payroll import Payroll
from util.util import DBConnUtil


class PayrollDAO:

    # Create
    def add_payroll(self, payroll):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Payroll 
                   (EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions, NetSalary)
                   VALUES (?, ?, ?, ?, ?, ?, ?)"""
        
        cursor.execute(query, (payroll.employee_id, payroll.start_date, payroll.end_date,
                               payroll.basic_salary, payroll.overtime_pay, payroll.deductions,
                               payroll.net_salary))
        
        # Get inserted PayrollID
        cursor.execute("SELECT SCOPE_IDENTITY()")
        payroll_id = cursor.fetchone()[0]
        
        conn.commit()
        conn.close()
        
        return payroll_id

    # Read By ID
    def get_payroll_by_id(self, payroll_id):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """SELECT PayrollID, EmployeeID, PayPeriodStartDate, PayPeriodEndDate, 
                          BasicSalary, OvertimePay, Deductions, NetSalary 
                   FROM Payroll WHERE PayrollID = ?"""
        
        cursor.execute(query, (payroll_id,))
        row = cursor.fetchone()
        conn.close()
        
        return Payroll(*row) if row else None

    # Read All
    def get_all_payrolls(self):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """SELECT PayrollID, EmployeeID, PayPeriodStartDate, PayPeriodEndDate, 
                          BasicSalary, OvertimePay, Deductions, NetSalary 
                   FROM Payroll"""
        
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        
        return [Payroll(*row) for row in rows]

    # Update
    def update_payroll(self, payroll):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """UPDATE Payroll 
                   SET EmployeeID = ?, PayPeriodStartDate = ?, PayPeriodEndDate = ?, 
                       BasicSalary = ?, OvertimePay = ?, Deductions = ?, NetSalary = ?
                   WHERE PayrollID = ?"""
        
        cursor.execute(query, (payroll.employee_id, payroll.start_date, payroll.end_date,
                               payroll.basic_salary, payroll.overtime_pay, payroll.deductions,
                               payroll.net_salary, payroll.payroll_id))
        
        conn.commit()
        conn.close()

    # Delete
    def delete_payroll(self, payroll_id):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM Payroll WHERE PayrollID = ?"
        cursor.execute(query, (payroll_id,))
        conn.commit()
        conn.close()


# Sample Test Run
if __name__ == "__main__":
    dao = PayrollDAO()

    # Get All Payroll Records
    payrolls = dao.get_all_payrolls()
    for p in payrolls:
        print(f"PayrollID: {p.payroll_id} | EmployeeID: {p.employee_id} | Net Salary: {p.net_salary}")
