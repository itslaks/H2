# Payroll Management System (PayXpert)

## 📌 Project Overview
The **Payroll Management System (PayXpert)** is a **Python** and **MSSQL-based** application designed to **manage employee payroll, tax calculations, and financial reporting** efficiently. It provides **CRUD operations** for employees, payroll processing, and tax calculations with structured database integration.

## 📌 Features
✅ **Employee Management** (Add, Retrieve, Update, Delete)
✅ **Payroll Processing** (Salary, Overtime, Deductions, Net Salary Calculation)
✅ **Tax Calculation** (Automated Tax Computation & Storage)
✅ **Financial Reporting** (Payroll and Tax Summary)
✅ **MSSQL Database Integration**
✅ **Exception Handling and Unit Testing**

---

## 📌 Technologies Used
- **Python 3.x** (Backend Logic)
- **Microsoft SQL Server (MSSQL)** (Database)
- **PyODBC** (Database Connectivity)
- **UnitTest** (Testing Framework)
- **Structured Exception Handling**

---

## 📌 Project Structure
```
PayrollManagementSystem/
│── database/               # Stores database-related files
│   ├── payxpert_schema.sql # SQL script for creating tables
│── entity/                 # Stores data models (No business logic here)
│   ├── Employee.py         # Employee class
│   ├── Payroll.py          # Payroll class
│   ├── Tax.py              # Tax class
│   ├── FinancialRecord.py  # FinancialRecord class
│── dao/                    # Data Access Layer (DB operations)
│   ├── Employeedao.py      # Handles Employee CRUD in DB
│   ├── Payrolldao.py       # Handles Payroll CRUD in DB
│   ├── Taxdao.py           # Handles Tax CRUD in DB
│   ├── Financialrecorddao.py     # Handles Financial Records CRUD in DB
│── service/                # Business Logic Layer
│   ├── EmployeeService.py  # Employee operations logic
│   ├── PayrollService.py   # Payroll calculations logic
│   ├── TaxService.py       # Tax calculations logic
│   ├── FinancialService.py # Financial operations logic
│── exception/              # Custom Exception Handling
│   ├── EmployeeNotFoundException.py
│   ├── PayrollGenerationException.py
│   ├── TaxCalculationException.py
│   ├── FinancialRecordException.py
│   ├── InvalidInputException.py
│   ├── DatabaseConnectionException.py
│── util/                   # Utilities (Helper functions, DB connection)
│   ├── DBConnUtil.py       # Handles database connection
│   ├── ValidationUtil.py   # Data validation functions
│── main/                   # Entry point for running the application
│   ├── MainModule.py       # CLI-based menu-driven application
│── reports/                # Stores generated financial reports
│   ├── salary_report.csv   # Example payroll report file
│── tests/                  # Unit Testing
│   ├── test_Employee.py    # Unit tests for EmployeeService
│   ├── test_Payroll.py     # Unit tests for PayrollService
│   ├── test_Tax.py         # Unit tests for TaxService
│── requirements.txt        # Python dependencies
│── README.md               # Documentation about the project

```

## 📌 Project Directory Structure
|-------------------------|---------------------------------------------------------------------|----------------------------------------------|
| **Folder/File**         | **Purpose**                                                         | **Example Files**                            |
|-------------------------|---------------------------------------------------------------------|----------------------------------------------|
| 📂 **database/**        | Contains SQL scripts for creating database tables.                 | `payxpert_schema.sql`                         |
| 📂 **entity/**          | Defines data models (Employee, Payroll, etc.) without business logic. | `Employee.py`, `Payroll.py`, `Tax.py`      |
| 📂 **dao/**             | Handles database operations (CRUD operations).                     | `EmployeeDAO.py`, `PayrollDAO.py`             |
| 📂 **service/**         | Contains business logic (Payroll calculation, Tax deduction, etc.). | `EmployeeService.py`, `PayrollService.py`    |
| 📂 **exception/**       | Custom exception handling classes.                                 | `DatabaseConnectionException.py`              |
| 📂 **util/**            | Contains utility files for database connection and input validation. | `DBConnUtil.py`                             |
| 📂 **main/**            | Entry point of the system, contains the menu-driven interface.      | `MainModule.py`                              |
| 📂 **reports/**         | Stores generated reports in CSV or PDF format.                     | `payroll_report.csv`, `tax_report.pdf`        |
| 📂 **tests/**           | Unit test files for testing services and DAOs.                     | `test_Employee.py`, `test_Payroll.py`         |
| 📄 **requirements.txt** | Lists required Python dependencies (like `pyodbc`).                 | `pyodbc`, `unittest`                         |
| 📄 **README.md**        | Documentation explaining the project and how to run it.             | Setup instructions, usage guide              |
|-------------------------|---------------------------------------------------------------------|---------------------------------------------- |

---

## 📌 Installation Guide
### **1️⃣ Prerequisites**
- Install **Python 3.x**
- Install **Microsoft SQL Server** (Ensure you have **MSSQL running**)
- Install dependencies

```bash
pip install -r requirements.txt
```

---

### **2️⃣ Setting up the Database**
1. Open **Microsoft SQL Server Management Studio (SSMS)**.
2. Run the SQL schema file to create tables:

```sql
database/PayXpert_schema.sql
```

3. Update **Database Connection Settings** in `util/DBConnUtil.py`:
```python
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=your_server;"
    "DATABASE=PayXpertDB;"
    "UID=your_user;"
    "PWD=your_password"
)
```

---

### **3️⃣ Running the Application**
Run the main module:
```bash
python main/MainModule.py
```

---

## 📌 Usage Guide
### **1️⃣ Employee Management**
- Add employees by entering details.
- View employee details.

### **2️⃣ Payroll Processing**
- Generate payroll by providing **salary, overtime, deductions**.
- View payroll reports.

### **3️⃣ Tax Calculation**
- Calculate tax based on **income and tax rules**.
- Store tax details for reporting.

---

## 📌 Unit Testing
Run unit tests to validate the functionalities:
```bash
python -m unittest discover tests
```



