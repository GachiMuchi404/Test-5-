import sqlite3

connector = sqlite3.connect("students.db")

cursor = connector.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               age INTEGER,
               grade TEXT NOT NULL)
''')

cursor.execute('''
INSERT INTO students (name,age,grade) VALUES ('Uygurskiy',16,'A')
               ''')
cursor.execute('''
INSERT INTO students (name,age,grade) VALUES ('Anna',15,'A')
               ''')
cursor.execute('''
INSERT INTO students (name,age,grade) VALUES ('Maria',17,'A')
               ''')
cursor.execute('''
INSERT INTO students (name,age,grade) VALUES ('Azara',15,'B')
               ''')
cursor.execute('''
INSERT INTO students (name,age,grade) VALUES ('Samsa',17,'D')
               ''')
cursor.execute('''
INSERT INTO students (name,age,grade) VALUES ('David',17,'F')
               ''')

# cursor.execute(" SELECT * FROM students")
# date = cursor.fetchall()


cursor.execute(" SELECT * FROM students WHERE grade = 'A'")
date_1 = cursor.fetchall()

connector.commit()
cursor.close()