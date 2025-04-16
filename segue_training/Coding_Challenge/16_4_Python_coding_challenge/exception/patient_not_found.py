class PatientNumberNotFoundException(Exception):
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.message = f"Patient with ID {patient_id} not found in the database"
        super().__init__(self.message)