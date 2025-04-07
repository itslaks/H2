import pyodbc
from entity.tax import Tax
from util.util import DBConnUtil


class TaxDAO:
    # Create
    def add_tax_record(self, tax):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Tax (EmployeeID, TaxYear, TaxableIncome, TaxAmount)
                   VALUES (?, ?, ?, ?)"""
        cursor.execute(query, (tax.employee_id, tax.tax_year, tax.taxable_income, tax.tax_amount))
        conn.commit()
        conn.close()

    # Read By ID
    def get_tax_by_id(self, tax_id):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Tax WHERE TaxID = ?"
        cursor.execute(query, (tax_id,))
        row = cursor.fetchone()
        conn.close()
        return Tax(*row) if row else None

    # Read All
    def get_all_taxes(self):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Tax"
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return [Tax(*row) for row in rows]

    # Update
    def update_tax_record(self, tax):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """UPDATE Tax 
                   SET EmployeeID = ?, TaxYear = ?, TaxableIncome = ?, TaxAmount = ?
                   WHERE TaxID = ?"""
        cursor.execute(query, (tax.employee_id, tax.tax_year, tax.taxable_income,
                               tax.tax_amount, tax.tax_id))
        conn.commit()
        conn.close()

    # Delete
    def delete_tax_record(self, tax_id):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM Tax WHERE TaxID = ?"
        cursor.execute(query, (tax_id,))
        conn.commit()
        conn.close()


# Sample Test Run
if __name__ == "__main__":
    dao = TaxDAO()

    # Get All Tax Records
    taxes = dao.get_all_taxes()
    for t in taxes:
        print(f"TaxID: {t.tax_id} | EmployeeID: {t.employee_id} | Tax Amount: {t.tax_amount}")
