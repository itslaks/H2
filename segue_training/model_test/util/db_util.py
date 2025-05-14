import pyodbc

class DBConnection:
    def __init__(self):  
        self.conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=HP_PAVILION\\SQLEXPRESS01;'  
            'DATABASE=PRACTICE;'
            'Trusted_Connection=yes;'
        )
        self.cursor = self.conn.cursor()

    def get_cursor(self):
        return self.cursor

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
