import pyodbc
from entity.FinancialRecord import FinancialRecord
from util.util import DBConnUtil


class FinancialDAO:

    # Create
    def add_financial_record(self, financial_record):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO FinancialRecord 
        (EmployeeID, RecordDate, Description, Amount, RecordType) 
        VALUES (?, ?, ?, ?, ?)"""
        
        cursor.execute(query, (financial_record.employee_id, financial_record.record_date,
                               financial_record.description, financial_record.amount,
                               financial_record.record_type))
        
        # Get inserted record_id
        cursor.execute("SELECT SCOPE_IDENTITY()")
        record_id = cursor.fetchone()[0]
        
        conn.commit()
        conn.close()
        
        return record_id

    # Read (By ID)
    def get_financial_record_by_id(self, record_id):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """SELECT RecordID, EmployeeID, RecordDate, Description, Amount, RecordType 
                   FROM FinancialRecord WHERE RecordID = ?"""
        cursor.execute(query, (record_id,))
        row = cursor.fetchone()
        conn.close()
        return FinancialRecord(*row) if row else None

    # Read (All)
    def get_all_financial_records(self):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """SELECT RecordID, EmployeeID, RecordDate, Description, Amount, RecordType 
                   FROM FinancialRecord"""
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return [FinancialRecord(*row) for row in rows]

    # Update
    def update_financial_record(self, financial_record):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = """UPDATE FinancialRecord 
                   SET EmployeeID = ?, RecordDate = ?, Description = ?, Amount = ?, RecordType = ? 
                   WHERE RecordID = ?"""
        cursor.execute(query, (financial_record.employee_id, financial_record.record_date,
                               financial_record.description, financial_record.amount,
                               financial_record.record_type, financial_record.record_id))
        conn.commit()
        conn.close()

    # Delete
    def delete_financial_record(self, record_id):
        conn = DBConnUtil.get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM FinancialRecord WHERE RecordID = ?"
        cursor.execute(query, (record_id,))
        conn.commit()
        conn.close()


# Sample Testing
if __name__ == "__main__":
    dao = FinancialDAO()

    # Fetch All Financial Records
    records = dao.get_all_financial_records()
    for record in records:
        print(f"{record.record_id}: {record.description} - {record.amount}")
