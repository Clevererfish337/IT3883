# Program Name: AdvAppAssignment5.py 
# Course: IT3883/Section WO1
# Student Name: Christopher Lee
# Assignment Number: Assignment# 5
# Due Date: 04/21/2026
# Purpose: What does the program do (in a few sentences)?  Code that creates and interacts with SQL by intaking data from an outside source.  
# List Specific resources used to complete the assignment.  Lecture notes and Copilot suggestions in Visual Studio.

import sqlite3 

# Create a connection
connection = sqlite3.connect("temperatures.db")
cursor = connection.cursor()    

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS temperatures (id INTEGER PRIMARY KEY AUTOINCREMENT, DayOfWeek TEXT NOT NULL, Temperature REAL NOT NULL)''')
connection.commit()

# Insert data into the table
InputFile = "Assignment5Input.txt"
with open(InputFile, 'r') as file:
    rows = []
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 2:
            continue
        day, temp = parts [0], float(parts [1])
        rows.append((day, temp))

cursor.executemany("INSERT INTO temperatures (DayOfWeek, Temperature) VALUES (?, ?)", rows)
connection.commit()
print(f"Entered {len(rows)} records.\n")

#calculate and print average temperature
for day in ("Sunday", "Thursday"):
    cursor.execute('''SELECT AVG(Temperature) FROM temperatures WHERE DayOfWeek = ?''', (day,))
    avg_temp = cursor.fetchone()[0]
    print(f"The average temperature for {day}: {avg_temp:.2f}")

connection.close()
