# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 06:13:22 2025

@author: juleigar
"""

import sqlite3

# Connect to SQLite (creates the file if it doesn't exist)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# 1. Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS python_programming (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    grade INTEGER NOT NULL
)
""")

# 2. Insert the rows
students = [
    (55, "Carl Davis", 61),
    (66, "Dennis Fredrickson", 88),
    (77, "Jane Richards", 78),
    (12, "Peyton Sawyer", 45),
    (2, "Lucas Brooke", 99)
]

cursor.executemany("INSERT OR IGNORE INTO python_programming VALUES (?, ?, ?)", students)

# 3. Select all records with grade between 60 and 80
print("\nStudents with grades between 60 and 80:")
cursor.execute("SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80")
for row in cursor.fetchall():
    print(row)

# 4. Change Carl Davis’s grade to 65
cursor.execute("UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis'")

# 5. Delete Dennis Fredrickson’s row
cursor.execute("DELETE FROM python_programming WHERE name = 'Dennis Fredrickson'")

# 6. Change grade of all students with id > 55 to 80
cursor.execute("UPDATE python_programming SET grade = 80 WHERE id > 55")

# Show final table
print("\nFinal state of table:")
cursor.execute("SELECT * FROM python_programming")
for row in cursor.fetchall():
    print(row)

# Save and close
conn.commit()
conn.close()
