import pyodbc
from entity.FinancialRecord import FinancialRecord
from util.util import DBConnUtil


class FinancialDAO:
    def add_financial_record(self, financial_record):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO FinancialRecord (EmployeeID, RecordDate, Description, Amount, RecordType)
                   VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(query, (financial_record.employee_id, financial_record.record_date,
                               financial_record.description, financial_record.amount,
                               financial_record.record_type))
        conn.commit()
        conn.close()
