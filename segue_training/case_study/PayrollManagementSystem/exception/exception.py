# Base Exception
class ApplicationException(Exception):
    def __init__(self, message="An application error occurred"):
        super().__init__(message)


# Thrown when Employee not found
class EmployeeNotFoundException(ApplicationException):
    def __init__(self, message="Employee not found in the system"):
        super().__init__(message)


# Thrown when Payroll generation fails
class PayrollGenerationException(ApplicationException):
    def __init__(self, message="Error occurred while generating payroll"):
        super().__init__(message)


# Thrown when Tax Calculation fails
class TaxCalculationException(ApplicationException):
    def __init__(self, message="Error occurred during tax calculation"):
        super().__init__(message)


# Thrown when Financial Record management fails
class FinancialRecordException(ApplicationException):
    def __init__(self, message="Error occurred while managing financial record"):
        super().__init__(message)


# Thrown when Invalid Input is provided
class InvalidInputException(ApplicationException):
    def __init__(self, message="Invalid input provided"):
        super().__init__(message)


# Thrown when Database Connection fails
class DatabaseConnectionException(ApplicationException):
    def __init__(self, message="Failed to connect to the database"):
        super().__init__(message)
