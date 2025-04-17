import pyodbc
from dao.ihospital_service import IHospitalService  
from entity.appointment import Appointment
from exception.patient_not_found import PatientNumberNotFoundException
from util.db_con import DBConnUtil

class HospitalServiceImpl(IHospitalService):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def getAppointmentById(self, appointment_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Appointment WHERE appointmentId = ?", appointment_id)
        row = cursor.fetchone()
        if row:
            return Appointment(row[0], row[1], row[2], row[3], row[4])
        return None

    def getAppointmentsForPatient(self, patient_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Appointment WHERE patientId = ?", patient_id)
        rows = cursor.fetchall()
        if not rows:
            raise PatientNumberNotFoundException(patient_id)
        appointments = []
        for row in rows:
            appointments.append(Appointment(row[0], row[1], row[2], row[3], row[4]))
        return appointments

    def getAppointmentsForDoctor(self, doctor_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Appointment WHERE doctorId = ?", doctor_id)
        rows = cursor.fetchall()
        appointments = []
        for row in rows:
            appointments.append(Appointment(row[0], row[1], row[2], row[3], row[4]))
        return appointments

    def scheduleAppointment(self, appointment):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO Appointment (appointmentId, patientId, doctorId, appointmentDate, description) VALUES (?, ?, ?, ?, ?)",
            (
                appointment.get_appointmentId(),
                appointment.get_patientId(),
                appointment.get_doctorId(),
                appointment.get_appointmentDate(),
                appointment.get_description()
            )
        )
        self.conn.commit()
        return True

    def updateAppointment(self, appointment):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE Appointment SET patientId = ?, doctorId = ?, appointmentDate = ?, description = ? WHERE appointmentId = ?",
            (
                appointment.get_patientId(),
                appointment.get_doctorId(),
                appointment.get_appointmentDate(),
                appointment.get_description(),
                appointment.get_appointmentId()
            )
        )
        self.conn.commit()
        return True

    def cancelAppointment(self, appointment_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Appointment WHERE appointmentId = ?", appointment_id)
        self.conn.commit()
        return True