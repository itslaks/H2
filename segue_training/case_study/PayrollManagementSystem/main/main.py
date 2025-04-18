from dao.employeedao import EmployeeDAO
from dao.payrolldao import PayrollDAO
from dao.taxdao import TaxDAO
from dao.financialrecorddao import FinancialDAO
from entity.employee import Employee
from entity.payroll import Payroll
from entity.tax import Tax
from entity.FinancialRecord import FinancialRecord
from exception.exception import (
    ApplicationException, 
    EmployeeNotFoundException, 
    PayrollGenerationException, 
    TaxCalculationException, 
    FinancialRecordException,
    InvalidInputException,
    DatabaseConnectionException
)


def display_record(record, title=None):
    """Helper function to display a record in a consistent format"""
    if title:
        print(f"\n--- {title} ---")
    
    record_id_field = None
    for field in ["employee_id", "payroll_id", "tax_id", "record_id"]:
        if hasattr(record, field) and getattr(record, field) is not None:
            record_id_field = field
            break
    
    if record_id_field:
        # Highlight the ID field with asterisks for better visibility
        print(f"\n*** {record_id_field.replace('_', ' ').title()}: {getattr(record, record_id_field)} ***")
    
    for field, value in vars(record).items():
        print(f"{field}: {value}")
    
    print("-" * 40)


def display_records(records, title=None):
    """Helper function to display multiple records in a consistent format"""
    if title:
        print(f"\n--- {title} ---")
    
    if not records:
        print("No records found.")
        return
    
    for record in records:
        display_record(record)


def confirm_action(message="Are you sure you want to proceed? (y/n): "):
    """Helper function to confirm critical actions"""
    response = input(message).strip().lower()
    return response == 'y' or response == 'yes'


def employee_menu():
    dao = EmployeeDAO()
    while True:
        print("\n--- Employee Menu ---")
        print("1. Add New Employee:")
        print("2. View Employee by ID:")
        print("3. View All Employees:")
        print("4. Update Employee:")
        print("5. Delete Employee:")
        print("6. Back to Main Menu")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                emp = Employee(
                    None,
                    input("First Name: "),
                    input("Last Name: "),
                    input("Date of Birth (YYYY-MM-DD): "),
                    input("Gender: "),
                    input("Email: "),
                    input("Phone Number: "),
                    input("Address: "),
                    input("Position: "),
                    input("Joining Date (YYYY-MM-DD): "),
                    input("Termination Date (YYYY-MM-DD or press Enter for None): ") or None
                )
                dao.add_employee(emp)
                print("\n✅ Employee added successfully!")
                
                # Display the newly added employee with its ID in a more visible format
                added_emp = dao.get_employee_by_id(emp.employee_id)
                if added_emp:
                    display_record(added_emp, "NEW EMPLOYEE RECORD - ASSIGNED ID")
                    print(f"\n📌 IMPORTANT: Remember employee ID #{added_emp.employee_id} for future reference!")

            elif choice == 2:
                emp_id = int(input("Enter Employee ID: "))
                emp = dao.get_employee_by_id(emp_id)
                if emp:
                    display_record(emp, "Employee Details")
                else:
                    raise EmployeeNotFoundException(f"Employee with ID {emp_id} not found.")

            elif choice == 3:
                employees = dao.get_all_employees()
                display_records(employees, "All Employees")

            elif choice == 4:
                emp_id = int(input("Enter Employee ID to Update: "))
                emp = dao.get_employee_by_id(emp_id)
                if emp:
                    display_record(emp, "Current Employee Details")
                    
                    print("\nSelect field to update (press Enter to keep current value):")
                    
                    new_first_name = input(f"First Name [{emp.first_name}]: ")
                    emp.first_name = new_first_name if new_first_name else emp.first_name
                    
                    new_last_name = input(f"Last Name [{emp.last_name}]: ")
                    emp.last_name = new_last_name if new_last_name else emp.last_name
                    
                    new_dob = input(f"Date of Birth [{emp.dob}]: ")
                    emp.dob = new_dob if new_dob else emp.dob
                    
                    new_gender = input(f"Gender [{emp.gender}]: ")
                    emp.gender = new_gender if new_gender else emp.gender
                    
                    new_email = input(f"Email [{emp.email}]: ")
                    emp.email = new_email if new_email else emp.email
                    
                    new_phone = input(f"Phone Number [{emp.phone}]: ")
                    emp.phone = new_phone if new_phone else emp.phone
                    
                    new_address = input(f"Address [{emp.address}]: ")
                    emp.address = new_address if new_address else emp.address
                    
                    new_position = input(f"Position [{emp.position}]: ")
                    emp.position = new_position if new_position else emp.position
                    
                    new_joining_date = input(f"Joining Date [{emp.joining_date}]: ")
                    emp.joining_date = new_joining_date if new_joining_date else emp.joining_date
                    
                    new_termination_date = input(f"Termination Date [{emp.termination_date or 'None'}]: ")
                    emp.termination_date = new_termination_date if new_termination_date else emp.termination_date
                    
                    if confirm_action("Save changes? (y/n): "):
                        dao.update_employee(emp)
                        print("\n✅ Employee updated successfully!")
                        # Display the updated employee with highlighted ID
                        updated_emp = dao.get_employee_by_id(emp_id)
                        display_record(updated_emp, "UPDATED EMPLOYEE RECORD")
                        print(f"\n📌 Employee ID #{updated_emp.employee_id} has been updated.")
                    else:
                        print("Update cancelled.")
                else:
                    raise EmployeeNotFoundException(f"Employee with ID {emp_id} not found.")

            elif choice == 5:
                emp_id = int(input("Enter Employee ID to Delete: "))
                emp = dao.get_employee_by_id(emp_id)
                if not emp:
                    raise EmployeeNotFoundException(f"Employee with ID {emp_id} not found.")
                
                display_record(emp, "Employee to Delete")
                if confirm_action("Are you sure you want to delete this employee? (y/n): "):
                    dao.delete_employee(emp_id)
                    print(f"\n✅ Employee with ID #{emp_id} deleted successfully.")
                else:
                    print("Deletion cancelled.")

            elif choice == 6:
                break

            else:
                print("Invalid Choice.")
        
        except ValueError:
            print("Please enter a valid number.")


def payroll_menu():
    dao = PayrollDAO()
    while True:
        print("\n--- Payroll Menu ---")
        print("1. Add New Payroll:")
        print("2. View Payroll by ID:")
        print("3. View All Payrolls:")
        print("4. Update Payroll:")
        print("5. Delete Payroll:")
        print("6. Back to Main Menu")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                pay = Payroll(
                    None,
                    int(input("Employee ID: ")),
                    input("Start Date (YYYY-MM-DD): "),
                    input("End Date (YYYY-MM-DD): "),
                    float(input("Basic Salary: ")),
                    float(input("Overtime Pay: ")),
                    float(input("Deductions: ")),
                    float(input("Net Salary: "))
                )
                dao.add_payroll(pay)
                print("\n✅ Payroll added successfully!")
                
                # Display the newly added payroll with its ID in a more visible format
                added_pay = dao.get_payroll_by_id(pay.payroll_id)
                if added_pay:
                    display_record(added_pay, "NEW PAYROLL RECORD - ASSIGNED ID")
                    print(f"\n📌 IMPORTANT: Remember payroll ID #{added_pay.payroll_id} for future reference!")

            elif choice == 2:
                pay_id = int(input("Enter Payroll ID: "))
                pay = dao.get_payroll_by_id(pay_id)
                if pay:
                    display_record(pay, "Payroll Details")
                else:
                    raise PayrollGenerationException(f"Payroll with ID {pay_id} not found.")

            elif choice == 3:
                payrolls = dao.get_all_payrolls()
                display_records(payrolls, "All Payrolls")

            elif choice == 4:
                pay_id = int(input("Enter Payroll ID to Update: "))
                pay = dao.get_payroll_by_id(pay_id)
                if pay:
                    display_record(pay, "Current Payroll Details")
                    
                    print("\nSelect field to update (press Enter to keep current value):")
                    
                    new_employee_id = input(f"Employee ID [{pay.employee_id}]: ")
                    pay.employee_id = int(new_employee_id) if new_employee_id else pay.employee_id
                    
                    new_start_date = input(f"Start Date [{pay.start_date}]: ")
                    pay.start_date = new_start_date if new_start_date else pay.start_date
                    
                    new_end_date = input(f"End Date [{pay.end_date}]: ")
                    pay.end_date = new_end_date if new_end_date else pay.end_date
                    
                    new_basic_salary = input(f"Basic Salary [{pay.basic_salary}]: ")
                    pay.basic_salary = float(new_basic_salary) if new_basic_salary else pay.basic_salary
                    
                    new_overtime_pay = input(f"Overtime Pay [{pay.overtime_pay}]: ")
                    pay.overtime_pay = float(new_overtime_pay) if new_overtime_pay else pay.overtime_pay
                    
                    new_deductions = input(f"Deductions [{pay.deductions}]: ")
                    pay.deductions = float(new_deductions) if new_deductions else pay.deductions
                    
                    new_net_salary = input(f"Net Salary [{pay.net_salary}]: ")
                    pay.net_salary = float(new_net_salary) if new_net_salary else pay.net_salary
                    
                    if confirm_action("Save changes? (y/n): "):
                        dao.update_payroll(pay)
                        print("\n✅ Payroll updated successfully!")
                        # Display the updated payroll with highlighted ID
                        updated_pay = dao.get_payroll_by_id(pay_id)
                        display_record(updated_pay, "UPDATED PAYROLL RECORD")
                        print(f"\n📌 Payroll ID #{updated_pay.payroll_id} has been updated.")
                    else:
                        print("Update cancelled.")
                else:
                    raise PayrollGenerationException(f"Payroll with ID {pay_id} not found.")

            elif choice == 5:
                pay_id = int(input("Enter Payroll ID to Delete: "))
                pay = dao.get_payroll_by_id(pay_id)
                if not pay:
                    raise PayrollGenerationException(f"Payroll with ID {pay_id} not found.")
                
                display_record(pay, "Payroll to Delete")
                if confirm_action("Are you sure you want to delete this payroll record? (y/n): "):
                    dao.delete_payroll(pay_id)
                    print(f"\n✅ Payroll with ID #{pay_id} deleted successfully.")
                else:
                    print("Deletion cancelled.")

            elif choice == 6:
                break

            else:
                print("Invalid Choice.")
        
        except ValueError:
            print("Please enter a valid number.")


def tax_menu():
    dao = TaxDAO()
    while True:
        print("\n--- Tax Menu ---")
        print("1. Add New Tax Record:")
        print("2. View Tax by ID:")
        print("3. View All Tax Records:")
        print("4. Update Tax Record:")
        print("5. Delete Tax Record:")
        print("6. Back to Main Menu:")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                tax = Tax(
                    None,
                    int(input("Employee ID: ")),
                    int(input("Tax Year: ")),
                    float(input("Taxable Income: ")),
                    float(input("Tax Amount: "))
                )
                dao.add_tax_record(tax)
                print("\n✅ Tax record added successfully!")
                
                # Display the newly added tax record with its ID in a more visible format
                added_tax = dao.get_tax_by_id(tax.tax_id)
                if added_tax:
                    display_record(added_tax, "NEW TAX RECORD - ASSIGNED ID")
                    print(f"\n📌 IMPORTANT: Remember tax ID #{added_tax.tax_id} for future reference!")

            elif choice == 2:
                tax_id = int(input("Enter Tax ID: "))
                tax = dao.get_tax_by_id(tax_id)
                if tax:
                    display_record(tax, "Tax Record Details")
                else:
                    raise TaxCalculationException(f"Tax record with ID {tax_id} not found.")

            elif choice == 3:
                taxes = dao.get_all_taxes()
                display_records(taxes, "All Tax Records")

            elif choice == 4:
                tax_id = int(input("Enter Tax ID to Update: "))
                tax = dao.get_tax_by_id(tax_id)
                if tax:
                    display_record(tax, "Current Tax Record Details")
                    
                    print("\nSelect field to update (press Enter to keep current value):")
                    
                    new_employee_id = input(f"Employee ID [{tax.employee_id}]: ")
                    tax.employee_id = int(new_employee_id) if new_employee_id else tax.employee_id
                    
                    new_tax_year = input(f"Tax Year [{tax.tax_year}]: ")
                    tax.tax_year = int(new_tax_year) if new_tax_year else tax.tax_year
                    
                    new_taxable_income = input(f"Taxable Income [{tax.taxable_income}]: ")
                    tax.taxable_income = float(new_taxable_income) if new_taxable_income else tax.taxable_income
                    
                    new_tax_amount = input(f"Tax Amount [{tax.tax_amount}]: ")
                    tax.tax_amount = float(new_tax_amount) if new_tax_amount else tax.tax_amount
                    
                    if confirm_action("Save changes? (y/n): "):
                        dao.update_tax_record(tax)
                        print("\n✅ Tax record updated successfully!")
                        # Display the updated tax record with highlighted ID
                        updated_tax = dao.get_tax_by_id(tax_id)
                        display_record(updated_tax, "UPDATED TAX RECORD")
                        print(f"\n📌 Tax ID #{updated_tax.tax_id} has been updated.")
                    else:
                        print("Update cancelled.")
                else:
                    raise TaxCalculationException(f"Tax record with ID {tax_id} not found.")

            elif choice == 5:
                tax_id = int(input("Enter Tax ID to Delete: "))
                tax = dao.get_tax_by_id(tax_id)
                if not tax:
                    raise TaxCalculationException(f"Tax record with ID {tax_id} not found.")
                
                display_record(tax, "Tax Record to Delete")
                if confirm_action("Are you sure you want to delete this tax record? (y/n): "):
                    dao.delete_tax_record(tax_id)
                    print(f"\n✅ Tax record with ID #{tax_id} deleted successfully.")
                else:
                    print("Deletion cancelled.")

            elif choice == 6:
                break

            else:
                print("Invalid Choice.")
        
        except ValueError:
            print("Please enter a valid number.")


def financial_record_menu():
    dao = FinancialDAO()
    while True:
        print("\n--- Financial Record Menu ---")
        print("1. Add New Financial Record")
        print("2. View Financial Record by ID")
        print("3. View All Financial Records")
        print("4. Update Financial Record")
        print("5. Delete Financial Record")
        print("6. Back to Main Menu")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                fr = FinancialRecord(
                    None,
                    int(input("Employee ID: ")),
                    input("Record Date (YYYY-MM-DD): "),
                    input("Description: "),
                    float(input("Amount: ")),
                    input("Record Type: ")
                )
                dao.add_financial_record(fr)
                print("\n✅ Financial record added successfully!")
                
                # Display the newly added financial record with its ID in a more visible format
                added_fr = dao.get_financial_record_by_id(fr.record_id)
                if added_fr:
                    display_record(added_fr, "NEW FINANCIAL RECORD - ASSIGNED ID")
                    print(f"\n📌 IMPORTANT: Remember financial record ID #{added_fr.record_id} for future reference!")

            elif choice == 2:
                fr_id = int(input("Enter Record ID: "))
                fr = dao.get_financial_record_by_id(fr_id)
                if fr:
                    display_record(fr, "Financial Record Details")
                else:
                    raise FinancialRecordException(f"Financial record with ID {fr_id} not found.")

            elif choice == 3:
                records = dao.get_all_financial_records()
                display_records(records, "All Financial Records")

            elif choice == 4:
                fr_id = int(input("Enter Record ID to Update: "))
                fr = dao.get_financial_record_by_id(fr_id)
                if fr:
                    display_record(fr, "Current Financial Record Details")
                    
                    print("\nSelect field to update (press Enter to keep current value):")
                    
                    new_employee_id = input(f"Employee ID [{fr.employee_id}]: ")
                    fr.employee_id = int(new_employee_id) if new_employee_id else fr.employee_id
                    
                    new_record_date = input(f"Record Date [{fr.record_date}]: ")
                    fr.record_date = new_record_date if new_record_date else fr.record_date
                    
                    new_description = input(f"Description [{fr.description}]: ")
                    fr.description = new_description if new_description else fr.description
                    
                    new_amount = input(f"Amount [{fr.amount}]: ")
                    fr.amount = float(new_amount) if new_amount else fr.amount
                    
                    new_record_type = input(f"Record Type [{fr.record_type}]: ")
                    fr.record_type = new_record_type if new_record_type else fr.record_type
                    
                    if confirm_action("Save changes? (y/n): "):
                        dao.update_financial_record(fr)
                        print("\n✅ Financial record updated successfully!")
                        # Display the updated financial record with highlighted ID
                        updated_fr = dao.get_financial_record_by_id(fr_id)
                        display_record(updated_fr, "UPDATED FINANCIAL RECORD")
                        print(f"\n📌 Financial Record ID #{updated_fr.record_id} has been updated.")
                    else:
                        print("Update cancelled.")
                else:
                    raise FinancialRecordException(f"Financial record with ID {fr_id} not found.")

            elif choice == 5:
                fr_id = int(input("Enter Record ID to Delete: "))
                fr = dao.get_financial_record_by_id(fr_id)
                if not fr:
                    raise FinancialRecordException(f"Financial record with ID {fr_id} not found.")
                
                display_record(fr, "Financial Record to Delete")
                if confirm_action("Are you sure you want to delete this financial record? (y/n): "):
                    dao.delete_financial_record(fr_id)
                    print(f"\n✅ Financial record with ID #{fr_id} deleted successfully.")
                else:
                    print("Deletion cancelled.")

            elif choice == 6:
                break

            else:
                print("Invalid Choice.")
        
        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        print("\n==== PayXpert Payroll Management System ====")
        print("1. View Employee Menu")
        print("2. View Payroll Menu")
        print("3. View Tax Menu")
        print("4. View Financial Record Menu")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                employee_menu()
            elif choice == 2:
                payroll_menu()
            elif choice == 3:
                tax_menu()
            elif choice == 4:
                financial_record_menu()
            elif choice == 5:
                if confirm_action("Are you sure you want to exit? (y/n): "):
                    print("Logging OUT...")
                    break
            else:
                print("Invalid Choice.")

        except EmployeeNotFoundException as e:
            print(f"Employee Error: {e}")
        except PayrollGenerationException as e:
            print(f"Payroll Error: {e}")
        except TaxCalculationException as e:
            print(f"Tax Error: {e}")
        except FinancialRecordException as e:
            print(f"Financial Record Error: {e}")
        except InvalidInputException as e:
            print(f"Input Error: {e}")
        except DatabaseConnectionException as e:
            print(f"Database Error: {e}")
        except ApplicationException as e:
            print(f"Application Error: {e}")
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()