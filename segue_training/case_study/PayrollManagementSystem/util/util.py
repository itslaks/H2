import pyodbc

class DBConnUtil:
    @staticmethod
    def get_connection():
        return pyodbc.connect(
    r"DRIVER={ODBC Driver 17 for SQL Server};"
    r"SERVER=HP_PAVILION\SQLEXPRESS01;" 
    r"DATABASE=PayXpert;"  
    r"Trusted_Connection=yes;"
)









