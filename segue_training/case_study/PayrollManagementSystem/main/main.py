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
                    print(vars(emp))
                else:
                    raise EmployeeNotFoundException(f"Employee with ID {emp_id} not found.")

            elif choice == 3:
                employees = dao.get_all_employees()
                if not employees:
                    print("No employees found.")
                else:
                    for emp in employees:
                        print(vars(emp))

            elif choice == 4:
                emp_id = int(input("Enter Employee ID to Update: "))
                emp = dao.get_employee_by_id(emp_id)
                if emp:
                    emp.first_name = input("First Name: ")
                    emp.last_name = input("Last Name: ")
                    emp.dob = input("Date of Birth (YYYY-MM-DD): ")
                    emp.gender = input("Gender: ")
                    emp.email = input("Email: ")
                    emp.phone = input("Phone Number: ")
                    emp.address = input("Address: ")
                    emp.position = input("Position: ")
                    emp.joining_date = input("Joining Date (YYYY-MM-DD): ")
                    emp.termination_date = input("Termination Date (YYYY-MM-DD or press Enter for None): ") or None
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
                    print(vars(pay))
                else:
                    raise PayrollGenerationException(f"Payroll with ID {pay_id} not found.")

            elif choice == 3:
                payrolls = dao.get_all_payrolls()
                if not payrolls:
                    print("No payroll records found.")
                else:
                    for pay in payrolls:
                        print(vars(pay))

            elif choice == 4:
                pay_id = int(input("Enter Payroll ID to Update: "))
                pay = dao.get_payroll_by_id(pay_id)
                if pay:
                    pay.employee_id = int(input("Employee ID: "))
                    pay.start_date = input("Start Date (YYYY-MM-DD): ")
                    pay.end_date = input("End Date (YYYY-MM-DD): ")
                    pay.basic_salary = float(input("Basic Salary: "))
                    pay.overtime_pay = float(input("Overtime Pay: "))
                    pay.deductions = float(input("Deductions: "))
                    pay.net_salary = float(input("Net Salary: "))
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
                    print(vars(tax))
                else:
                    raise TaxCalculationException(f"Tax record with ID {tax_id} not found.")

            elif choice == 3:
                taxes = dao.get_all_tax_records()
                if not taxes:
                    print("No tax records found.")
                else:
                    for tax in taxes:
                        print(vars(tax))

            elif choice == 4:
                tax_id = int(input("Enter Tax ID to Update: "))
                tax = dao.get_tax_by_id(tax_id)
                if tax:
                    tax.employee_id = int(input("Employee ID: "))
                    tax.tax_year = int(input("Tax Year: "))
                    tax.taxable_income = float(input("Taxable Income: "))
                    tax.tax_amount = float(input("Tax Amount: "))
                    dao.update_tax_record(tax)
                    print("Tax record updated successfully.")
                else:
                    # Fixed: Using TaxCalculationException instead of ApplicationException
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
                    print(vars(fr))
                else:
                    raise FinancialRecordException(f"Financial record with ID {fr_id} not found.")

            elif choice == 3:
                records = dao.get_all_financial_records()
                if not records:
                    print("No financial records found.")
                else:
                    for fr in records:
                        print(vars(fr))

            elif choice == 4:
                fr_id = int(input("Enter Record ID to Update: "))
                fr = dao.get_financial_record_by_id(fr_id)
                if fr:
                    fr.employee_id = int(input("Employee ID: "))
                    fr.record_date = input("Record Date (YYYY-MM-DD): ")
                    fr.description = input("Description: ")
                    fr.amount = float(input("Amount: "))
                    fr.record_type = input("Record Type: ")
                    dao.update_financial_record(fr)
                    print("Financial record updated successfully.")
                else:
                    # Fixed: Using FinancialRecordException instead of ApplicationException
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