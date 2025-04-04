import pyodbc
from entity.payroll import Payroll
from util.util import DBConnUtil

class PayrollDAO:
    def add_payroll(self, payroll):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Payroll (EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions, NetSalary)
                   VALUES (?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(query, (payroll.employee_id, payroll.start_date, payroll.end_date,
                               payroll.basic_salary, payroll.overtime_pay, payroll.deductions,
                               payroll.net_salary))
        conn.commit()
        conn.close()

    def get_payroll_by_id(self, payroll_id):  
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Payroll WHERE PayrollID = ?"  
        cursor.execute(query, (payroll_id,))
        row = cursor.fetchone()
        conn.close()
        return Payroll(*row) if row else None


dao = PayrollDAO()
payroll = dao.get_payroll_by_id(1)
if payroll:
    print(f"Payroll Found: {payroll.employee_id} {payroll.start_date} {payroll.end_date}")
else:
    print("Payroll record not found.")
