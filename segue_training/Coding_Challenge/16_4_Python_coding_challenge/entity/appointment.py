class Appointment:
    def __init__(self, appointmentId, patientId, doctorId, appointmentDate, description):
        self.appointmentId = appointmentId
        self.patientId = patientId
        self.doctorId = doctorId
        self.appointmentDate = appointmentDate
        self.description = description

    def get_appointmentId(self):
        return self.appointmentId
    
    def set_appointmentId(self, appointmentId):
        self.appointmentId = appointmentId
    
    def get_patientId(self):
        return self.patientId
    
    def set_patientId(self, patientId):
        self.patientId = patientId
    
    def get_doctorId(self):
        return self.doctorId
    
    def set_doctorId(self, doctorId):
        self.doctorId = doctorId
    
    def get_appointmentDate(self):
        return self.appointmentDate
    
    def set_appointmentDate(self, appointmentDate):
        self.appointmentDate = appointmentDate
    
    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description
    
    def __str__(self):
        return f"Appointment [ID: {self.appointmentId}, Patient: {self.patientId}, Doctor: {self.doctorId}, Date: {self.appointmentDate}, Description: {self.description}]"