import pyodbc
from util.db_property_util import PropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection():
        conn_str = PropertyUtil.get_property_string()
        return pyodbc.connect(conn_str)
