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


def employee_menu():
    dao = EmployeeDAO()
    while True:
        print("\n--- Employee Menu ---")
        print("1. Add Employee")
        print("2. View Employee by ID")
        print("3. View All Employees")
        print("4. Update Employee")
        print("5. Delete Employee")
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
                print("Employee added successfully.")

            elif choice == 2:
                emp_id = int(input("Enter Employee ID: "))
                emp = dao.get_employee_by_id(emp_id)
                if emp:
                    print(f"\nEmployee ID: {emp.employee_id}")
                    for field, value in vars(emp).items():
                        print(f"{field}: {value}")
                else:
                    raise EmployeeNotFoundException(f"Employee with ID {emp_id} not found.")

            elif choice == 3:
                employees = dao.get_all_employees()
                if not employees:
                    print("No employees found.")
                else:
                    for emp in employees:
                        print(f"\nEmployee ID: {emp.employee_id}")
                        for field, value in vars(emp).items():
                            print(f"{field}: {value}")
                        print("-" * 40)

            elif choice == 4:
                emp_id = int(input("Enter Employee ID to Update: "))
                emp = dao.get_employee_by_id(emp_id)
                if emp:
                    print("\nCurrent Employee Details:")
                    print(f"Employee ID: {emp.employee_id}")
                    for field, value in vars(emp).items():
                        print(f"{field}: {value}")
                    
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
                    
                    dao.update_employee(emp)
                    print("Employee updated successfully.")
                else:
                    raise EmployeeNotFoundException(f"Employee with ID {emp_id} not found.")

            elif choice == 5:
                emp_id = int(input("Enter Employee ID to Delete: "))
                emp = dao.get_employee_by_id(emp_id)
                if not emp:
                    raise EmployeeNotFoundException(f"Employee with ID {emp_id} not found.")
                dao.delete_employee(emp_id)
                print("Employee deleted successfully.")

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
        print("1. Add Payroll")
        print("2. View Payroll by ID")
        print("3. View All Payrolls")
        print("4. Update Payroll")
        print("5. Delete Payroll")
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
                print("Payroll added successfully.")

            elif choice == 2:
                pay_id = int(input("Enter Payroll ID: "))
                pay = dao.get_payroll_by_id(pay_id)
                if pay:
                    print(f"\nPayroll ID: {pay.payroll_id}")
                    for field, value in vars(pay).items():
                        print(f"{field}: {value}")
                else:
                    raise PayrollGenerationException(f"Payroll with ID {pay_id} not found.")

            elif choice == 3:
                payrolls = dao.get_all_payrolls()
                if not payrolls:
                    print("No payroll records found.")
                else:
                    for pay in payrolls:
                        print(f"\nPayroll ID: {pay.payroll_id}")
                        for field, value in vars(pay).items():
                            print(f"{field}: {value}")
                        print("-" * 40)

            elif choice == 4:
                pay_id = int(input("Enter Payroll ID to Update: "))
                pay = dao.get_payroll_by_id(pay_id)
                if pay:
                    print("\nCurrent Payroll Details:")
                    print(f"Payroll ID: {pay.payroll_id}")
                    for field, value in vars(pay).items():
                        print(f"{field}: {value}")
                    
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
                    
                    dao.update_payroll(pay)
                    print("Payroll updated successfully.")
                else:
                    raise PayrollGenerationException(f"Payroll with ID {pay_id} not found.")

            elif choice == 5:
                pay_id = int(input("Enter Payroll ID to Delete: "))
                pay = dao.get_payroll_by_id(pay_id)
                if not pay:
                    raise PayrollGenerationException(f"Payroll with ID {pay_id} not found.")
                dao.delete_payroll(pay_id)
                print("Payroll deleted successfully.")

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
        print("1. Add Tax Record")
        print("2. View Tax by ID")
        print("3. View All Tax Records")
        print("4. Update Tax Record")
        print("5. Delete Tax Record")
        print("6. Back to Main Menu")

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
                print("Tax record added successfully.")

            elif choice == 2:
                tax_id = int(input("Enter Tax ID: "))
                tax = dao.get_tax_by_id(tax_id)
                if tax:
                    print(f"\nTax ID: {tax.tax_id}")
                    for field, value in vars(tax).items():
                        print(f"{field}: {value}")
                else:
                    raise TaxCalculationException(f"Tax record with ID {tax_id} not found.")

            elif choice == 3:
                taxes = dao.get_all_tax_records()
                if not taxes:
                    print("No tax records found.")
                else:
                    for tax in taxes:
                        print(f"\nTax ID: {tax.tax_id}")
                        for field, value in vars(tax).items():
                            print(f"{field}: {value}")
                        print("-" * 40)

            elif choice == 4:
                tax_id = int(input("Enter Tax ID to Update: "))
                tax = dao.get_tax_by_id(tax_id)
                if tax:
                    print("\nCurrent Tax Record Details:")
                    print(f"Tax ID: {tax.tax_id}")
                    for field, value in vars(tax).items():
                        print(f"{field}: {value}")
                    
                    print("\nSelect field to update (press Enter to keep current value):")
                    
                    new_employee_id = input(f"Employee ID [{tax.employee_id}]: ")
                    tax.employee_id = int(new_employee_id) if new_employee_id else tax.employee_id
                    
                    new_tax_year = input(f"Tax Year [{tax.tax_year}]: ")
                    tax.tax_year = int(new_tax_year) if new_tax_year else tax.tax_year
                    
                    new_taxable_income = input(f"Taxable Income [{tax.taxable_income}]: ")
                    tax.taxable_income = float(new_taxable_income) if new_taxable_income else tax.taxable_income
                    
                    new_tax_amount = input(f"Tax Amount [{tax.tax_amount}]: ")
                    tax.tax_amount = float(new_tax_amount) if new_tax_amount else tax.tax_amount
                    
                    dao.update_tax_record(tax)
                    print("Tax record updated successfully.")
                else:
                    raise TaxCalculationException(f"Tax record with ID {tax_id} not found.")

            elif choice == 5:
                tax_id = int(input("Enter Tax ID to Delete: "))
                tax = dao.get_tax_by_id(tax_id)
                if not tax:
                    raise TaxCalculationException(f"Tax record with ID {tax_id} not found.")
                dao.delete_tax_record(tax_id)
                print("Tax record deleted successfully.")

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
        print("1. Add Financial Record")
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
                print("Financial record added successfully.")

            elif choice == 2:
                fr_id = int(input("Enter Record ID: "))
                fr = dao.get_financial_record_by_id(fr_id)
                if fr:
                    print(f"\nFinancial Record ID: {fr.record_id}")
                    for field, value in vars(fr).items():
                        print(f"{field}: {value}")
                else:
                    raise FinancialRecordException(f"Financial record with ID {fr_id} not found.")

            elif choice == 3:
                records = dao.get_all_financial_records()
                if not records:
                    print("No financial records found.")
                else:
                    for fr in records:
                        print(f"\nFinancial Record ID: {fr.record_id}")
                        for field, value in vars(fr).items():
                            print(f"{field}: {value}")
                        print("-" * 40)

            elif choice == 4:
                fr_id = int(input("Enter Record ID to Update: "))
                fr = dao.get_financial_record_by_id(fr_id)
                if fr:
                    print("\nCurrent Financial Record Details:")
                    print(f"Financial Record ID: {fr.record_id}")
                    for field, value in vars(fr).items():
                        print(f"{field}: {value}")
                    
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
                    
                    dao.update_financial_record(fr)
                    print("Financial record updated successfully.")
                else:
                    raise FinancialRecordException(f"Financial record with ID {fr_id} not found.")

            elif choice == 5:
                fr_id = int(input("Enter Record ID to Delete: "))
                fr = dao.get_financial_record_by_id(fr_id)
                if not fr:
                    raise FinancialRecordException(f"Financial record with ID {fr_id} not found.")
                dao.delete_financial_record(fr_id)
                print("Financial record deleted successfully.")

            elif choice == 6:
                break

            else:
                print("Invalid Choice.")
        
        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        print("\n==== PayXpert Payroll Management System ====")
        print("1. Employee Menu")
        print("2. Payroll Menu")
        print("3. Tax Menu")
        print("4. Financial Record Menu")
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
                print("Exiting... Thank You!")
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
