import sqlite3
#backend

def patientData():
    con=sqlite3.connect("patient.db")
    cur= con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StdID text, Firstname text, Surname text,DoB text, Age text, Gender text, Address text,Mobile text)")
    con.commit()
    con.close()
