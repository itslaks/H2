class Doctor:
    def __init__(self, doctorId=0, firstName="", lastName="", specialization="", contactNumber=""):
        self.__doctorId = doctorId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__specialization = specialization
        self.__contactNumber = contactNumber

    def get_doctorId(self): return self.__doctorId
    def set_doctorId(self, value): self.__doctorId = value

    def get_firstName(self): return self.__firstName
    def set_firstName(self, value): self.__firstName = value

    def get_lastName(self): return self.__lastName
    def set_lastName(self, value): self.__lastName = value

    def get_specialization(self): return self.__specialization
    def set_specialization(self, value): self.__specialization = value

    def get_contactNumber(self): return self.__contactNumber
    def set_contactNumber(self, value): self.__contactNumber = value

    def __str__(self):
        return f"{self.__doctorId}, {self.__firstName}, {self.__lastName}, {self.__specialization}, {self.__contactNumber}"
