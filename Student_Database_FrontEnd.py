#Frontend

from tkinter import*
import tkinter.messagebox
import patDatabase_BackEnd
import tkinter.ttk as ttk 


class Patient:

    def __init__(self,root):
        self.root = root
        self.root.title("Patient Records System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="skyblue")
    
        PID = StringVar()
        Name = StringVar()
        DOB = StringVar()
        Sex = StringVar()
        Bloodgroup = StringVar()
        Cash = StringVar()
        Address = StringVar()
        Mobile = StringVar()

        def iExit():
            iExit = tkinter.messagebox.askyesno("Patient Records System","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtPID.delete(0,END)
            self.txtna.delete(0,END)
            self.txtDOB.delete(0,END)
            self.txtSex.delete(0,END)
            self.txtBloodgroup.delete(0,END)
            self.txtCash.delete(0,END)
            self.txtAdr.delete(0,END)
            self.txtMobile.delete(0,END)


        def addData():
            if(len(PID.get())!=0):
                patDatabase_BackEnd.addPatRec(PID.get(), Name.get(),DOB.get(),Sex.get(),Bloodgroup.get(),Address.get(),Mobile.get(),Cash.get())
                patientlist.delete(0,END)
                patientlist.insert(END,(PID.get(), Name.get(),DOB.get(),Sex.get(),Bloodgroup.get(),Address.get(),Mobile.get(),Cash.get()))

        def DisplayData():
            patientlist.delete(0,END)
            for row in patDatabase_BackEnd.viewData():
              patientlist.insert(END,row,str(""))
