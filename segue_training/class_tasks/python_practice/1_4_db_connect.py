import pyodbc


conn = pyodbc.connect(
    r"DRIVER={ODBC Driver 17 for SQL Server};"
    r"SERVER=HP_PAVILION\SQLEXPRESS01;" 
    r"DATABASE=myproject;"  
    r"Trusted_Connection=yes;"
)


cursor = conn.cursor()

cursor.execute("""
    INSERT INTO Quiz_Questions (question, option_a, option_b, option_c, option_d, correct_option)
    VALUES (?, ?, ?, ?, ?, ?)
""", ("What is the correct extension of python?", ".python", ".pyx", ".py", ".program", "C"))


cursor.execute("""
    INSERT INTO Player_Score (player_name, score)
    VALUES (?, ?)
""", ("Harish", 50))

# Insert data into the Execution_Logs table
cursor.execute("""
    INSERT INTO Execution_Logs (event_description, timestamp)
    VALUES (?, ?)
""", ("New record inserted into tables", "2025-04-01 12:00:00"))

# Commit the transactions
conn.commit()

print("Values inserted successfully!")

# Close the connection
conn.close()




