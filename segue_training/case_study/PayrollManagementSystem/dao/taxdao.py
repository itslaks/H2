import pyodbc
from entity.tax import Tax
from util.util import DBConnUtil

class TaxDAO:
    def add_tax_record(self, tax):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Tax (EmployeeID, TaxYear, TaxableIncome, TaxAmount)
                   VALUES (?, ?, ?, ?)"""
        cursor.execute(query, (tax.employee_id, tax.tax_year, tax.taxable_income, tax.tax_amount))
        conn.commit()
        conn.close()
