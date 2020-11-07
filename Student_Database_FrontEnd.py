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
        
        scrollbar = Scrollbar(DataFrame2, orient="vertical")
        scrollbar.grid(row=0,column=1,sticky='ns')
        patientlist = Listbox(DataFrame2, width=110, height=5, font=('arial',12,'bold'), yscrollcommand=scrollbar.set)
        patientlist.bind('<<ListboxSelect>>', PatientRec)
        patientlist.grid(row=0,column=8,padx=8)
        scrollbar.config(command = patientlist.yview)
        
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
            
         
        def PatientRec(event):
            global sd
            searchStd= patientlist.curselection()[0]
            sd= patientlist.get(searchStd)


            self.txtPID.delete(0,END)
            self.txtPID.insert(END,sd[1])
            self.txtna.delete(0,END)
            self.txtna.insert(END,sd[2])
            self.txtDOB.delete(0,END)
            self.txtDOB.insert(END,sd[3])
            self.txtSex.delete(0,END)
            self.txtSex.insert(END,sd[4])
            self.txtBloodgroup.delete(0,END)
            self.txtBloodgroup.insert(END,sd[5])
            self.txtCash.delete(0,END)
            self.txtCash.insert(END,sd[6])
            self.txtAdr.delete(0,END)
            self.txtAdr.insert(END,sd[7])
            self.txtMobile.delete(0,END)
            self.txtMobile.insert(END,sd[8])

        def DeleteData():
            if(len(PID.get())!=0):
                patDatabase_BackEnd.deleteRec(sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
             patientlist.delete(0,END)
             for row in patDatabase_BackEnd.searchData(PID.get(), Name.get(),DOB.get(),Sex.get(),Bloodgroup.get(),Address.get(),Mobile.get(),Cash.get()):
                 patientlist.insert(END,row,str(""))

        def update():
            if(len(PID.get())!=0):
                patDatabase_BackEnd.deleteRec(sd[0])
            if(len(PID.get())!=0):
                patDatabase_BackEnd.addPatRec(PID.get(), Name.get(),DOB.get(),Sex.get(),Bloodgroup.get(), Address.get(),Mobile.get(),Cash.get())
                patientlist.delete(0,END)
                patientlist.insert(END,(PID.get(), Name.get(),DOB.get(),Sex.get(),Bloodgroup.get(),Address.get(),Mobile.get(),Cash.get())
