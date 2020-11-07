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
def viewData():
    con=sqlite3.connect("patient.db")
    cur =con.cursor()
    cur.execute("SELECT * FROM patient")
    row =cur.fetchall()
    con.close
    return row

def deleteRec(id):
    con=sqlite3.connect("patient.db")
    cur =con.cursor()
    cur.execute("DELETE FROM patient WHERE id=?",(id,))
    con.commit()
    con.close

def searchData(PID="",Name="",DOB="",Sex="",Bloodgroup="",Address="",Mobile="",Cash=""):
    con=sqlite3.connect("patient.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM patient WHERE PID=? OR Name=? OR DOB=? OR Sex=? OR Bloodgroup=? OR Address=? OR  Mobile=? OR Cash=?", (PID , Name, DOB, Sex, Bloodgroup, Address ,Mobile, Cash))
    rows=cur.fetchall()
    con.close()
    return rows
def dataUpdate(id,PID="",Name="",DOB="",Sex="",Bloodgroup="",Address="",Mobile="",Cash=""):
    con=sqlite3.connect("patient.db")
    cur = con.cursor()
    cur.execute("UPDATE patient SET PID=?,Name=?,DOB=?,Sex=?,Bloodgroup=?,Address=?,Mobile=?,Cash=?, WHERE id=?", (PID , Name, DOB, Sex, Bloodgroup, Address ,Mobile, Cash,id))
    con.commit()
    con.close()


patientData()
