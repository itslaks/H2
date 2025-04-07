class ApplicationException(Exception):
    def __init__(self, message="An application error occurred"):
        super().__init__(message)
