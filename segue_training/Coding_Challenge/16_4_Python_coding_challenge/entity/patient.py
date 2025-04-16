class Patient:
    def __init__(self, patientId=0, firstName="", lastName="", dateOfBirth="", gender="", contactNumber="", address=""):
        self.__patientId = patientId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__dateOfBirth = dateOfBirth
        self.__gender = gender
        self.__contactNumber = contactNumber
        self.__address = address

    def get_patientId(self): return self.__patientId
    def set_patientId(self, value): self.__patientId = value

    def get_firstName(self): return self.__firstName
    def set_firstName(self, value): self.__firstName = value

    def get_lastName(self): return self.__lastName
    def set_lastName(self, value): self.__lastName = value

    def get_dateOfBirth(self): return self.__dateOfBirth
    def set_dateOfBirth(self, value): self.__dateOfBirth = value

    def get_gender(self): return self.__gender
    def set_gender(self, value): self.__gender = value

    def get_contactNumber(self): return self.__contactNumber
    def set_contactNumber(self, value): self.__contactNumber = value

    def get_address(self): return self.__address
    def set_address(self, value): self.__address = value

    def __str__(self):
        return f"{self.__patientId}, {self.__firstName}, {self.__lastName}, {self.__dateOfBirth}, {self.__gender}, {self.__contactNumber}, {self.__address}"
