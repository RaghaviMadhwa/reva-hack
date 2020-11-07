import sqlite3
#backend


import sqlite3
#backend

def patientData():
    con=sqlite3.connect("patient.db")
    cur= con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS patient(id INTEGER PRIMARY KEY, PID text, Name text, DOB text, Sex text, Bloodgroup text, Address text, Mobile text, Cash text)")
    con.commit()
    con.close()

def addPatRec(PID , Name, DOB, Sex, Bloodgroup, Address ,Mobile, Cash):
    con=sqlite3.connect("patient.db")
    cur =con.cursor()
    cur.execute("INSERT INTO patient VALUES (NULL, ?,?,?,?,?,?,?,?)",(PID , Name, DOB, Sex, Bloodgroup, Address ,Mobile, Cash))
    con.commit()
    con.close()
