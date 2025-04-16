import sys
import os
import datetime

# Adding the root directory to sys.path to resolve imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dao.hospital_service_imple import HospitalServiceImpl
from entity.appointment import Appointment
from exception.patient_not_found import PatientNumberNotFoundException

def validate_date(date_str):
    """Validate that the date string is in the format YYYY-MM-DD"""
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def get_valid_integer(prompt):
    """Get a valid integer input from the user"""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def main():
    service = HospitalServiceImpl()

    while True:
        print("\n--- Hospital Management System ---")
        print("1. Get Appointment by Appointment ID")
        print("2. Get Appointments for Patient ID")
        print("3. Get Appointments for Doctor ID ")
        print("4. Schedule new Appointment")
        print("5. Update Exisiting Appointment")
        print("6. Cancel Appointment")
        print("7. Exit")
        choice = input("Enter choice: ")

        try:
            if choice == '1':
                aid = get_valid_integer("Enter Appointment ID: ")
                appt = service.getAppointmentById(aid)
                if appt:
                    print("\nAppointment Details:")
                    print(appt)
                else:
                    print("Appointment not found.")

            elif choice == '2':
                pid = get_valid_integer("Enter Patient ID: ")
                try:
                    appts = service.getAppointmentsForPatient(pid)
                    if appts:
                        print(f"\nAppointments for Patient #{pid}:")
                        for a in appts:
                            print(a)
                    else:
                        print(f"No appointments found for Patient #{pid}.")
                except PatientNumberNotFoundException as e:
                    print(f"Error: Patient with ID {pid} not found.")

            elif choice == '3':
                did = get_valid_integer("Enter Doctor ID: ")
                try:
                    appts = service.getAppointmentsForDoctor(did)
                    if appts:
                        print(f"\nAppointments for Doctor #{did}:")
                        for a in appts:
                            print(a)
                    else:
                        print(f"No appointments found for Doctor #{did}.")
                except Exception as e:
                    print(f"Error retrieving appointments for Doctor #{did}: {e}")

            elif choice == '4':
                try:
                    aid = get_valid_integer("Enter Appointment ID: ")
                    # Check if appointment ID already exists
                    if service.getAppointmentById(aid):
                        print(f"Error: Appointment with ID {aid} already exists.")
                        continue
                        
                    pid = get_valid_integer("Enter Patient ID: ")
                    did = get_valid_integer("Enter Doctor ID: ")
                    
                    while True:
                        date = input("Enter Appointment Date (YYYY-MM-DD): ")
                        if validate_date(date):
                            break
                        print("Invalid date format. Please use YYYY-MM-DD format.")
                    
                    description = input("Enter Appointment Description: ")

                    appointment = Appointment(aid, pid, did, date, description)
                    success = service.scheduleAppointment(appointment)
                    print("Appointment scheduled successfully." if success else "Failed to schedule appointment.")
                except Exception as e:
                    print(f"Error scheduling appointment: {e}")

            elif choice == '5':
                try:
                    aid = get_valid_integer("Enter Appointment ID to update: ")
                    appt = service.getAppointmentById(aid)
                    if not appt:
                        print(f"Error: Appointment with ID {aid} not found.")
                        continue
                        
                    print("\nCurrent Appointment Details:")
                    print(appt)
                    print("\nEnter new details (press Enter to keep current value):")
                    
                    # Patient ID
                    pid_input = input(f"Enter New Patient ID [{appt.get_patientId()}]: ")
                    pid = int(pid_input) if pid_input else appt.get_patientId()
                    
                    # Doctor ID
                    did_input = input(f"Enter New Doctor ID [{appt.get_doctorId()}]: ")
                    did = int(did_input) if did_input else appt.get_doctorId()
                    
                    # Date
                    while True:
                        date_input = input(f"Enter New Appointment Date [{appt.get_appointmentDate()}]: ")
                        date = date_input if date_input else appt.get_appointmentDate()
                        if not date_input or validate_date(date):
                            break
                        print("Invalid date format. Please use YYYY-MM-DD format.")
                    
                    # Description
                    desc_input = input(f"Enter New Description [{appt.get_description()}]: ")
                    description = desc_input if desc_input else appt.get_description()
                    
                    # Confirm changes
                    print("\nNew Appointment Details:")
                    print(f"Appointment ID: {aid}")
                    print(f"Patient ID: {pid}")
                    print(f"Doctor ID: {did}")
                    print(f"Date: {date}")
                    print(f"Description: {description}")
                    
                    confirm = input("\nSave these changes? (y/n): ").lower()
                    if confirm == 'y':
                        # Create a new appointment object with updated values
                        updated_appointment = Appointment(aid, pid, did, date, description)
                        success = service.updateAppointment(updated_appointment)
                        print("Appointment updated successfully." if success else "Failed to update appointment.")
                    else:
                        print("Update cancelled.")
                except Exception as e:
                    print(f"Error updating appointment: {e}")

            elif choice == '6':
                try:
                    aid = get_valid_integer("Enter Appointment ID to cancel: ")
                    appt = service.getAppointmentById(aid)
                    if not appt:
                        print(f"Error: Appointment with ID {aid} not found.")
                        continue
                        
                    print("\nAppointment to cancel:")
                    print(appt)
                    confirm = input("\nAre you sure you want to cancel this appointment? (y/n): ").lower()
                    if confirm == 'y':
                        success = service.cancelAppointment(aid)
                        print("Appointment cancelled successfully." if success else "Failed to cancel appointment.")
                    else:
                        print("Cancellation aborted.")
                except Exception as e:
                    print(f"Error cancelling appointment: {e}")

            elif choice == '7':
                print("Thank you for using the Hospital Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

        except PatientNumberNotFoundException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {str(e)}")
            
    # Close the database connection when exiting
    try:
        service.conn.close()
        print("Database connection closed.")
    except:
        pass

if __name__ == '__main__':
    main()