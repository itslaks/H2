class PropertyUtil:
    @staticmethod
    def get_property_string():
        return (
            r"DRIVER={ODBC Driver 17 for SQL Server};"
            r"SERVER=HP_PAVILION\SQLEXPRESS01;"
            r"DATABASE=HospitalManagementSystem;"
            r"Trusted_Connection=yes;"
        )
