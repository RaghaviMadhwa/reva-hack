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
        
        
        MainFrame = Frame(self.root,bg="tan")
        MainFrame.grid()  

        TitFrame=Frame(MainFrame,bd=10, padx=90, pady=8, bg="papayawhip", relief= RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit=Label(TitFrame, width= 55, font=('arial',30,'bold'), text="Patient Records System", bg="papayawhip")
        self.lblTit.grid()

        ButtonFrame=Frame(MainFrame,bd=10, width=2000, height=60, padx=18, pady=20, bg="papayawhip", relief= RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bd=9, width=2000, height=120, padx=40, pady=40, bg="papayawhip", relief= RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrame1=LabelFrame(DataFrame,bd=6, width= 900, height=4, padx=1, bg="papayawhip", relief= RIDGE, text="Patient Info\n",font=('arial',20,'bold'))
        DataFrame1.pack(side=TOP)

        DataFrame2=LabelFrame(DataFrame,bd=6, width=900, height=16, padx=1, bg="papayawhip", relief= RIDGE,text="Patient Details\n",font=('arial',20,'bold'))
        DataFrame2.pack(side=TOP)
        
        
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

                                     
                                      
                                   
        self.btnAddDate = Button(ButtonFrame, text="Add New",  font=('arial',20,'bold'), width=12, height=1, bd=4, command=addData)
        self.btnAddDate.grid(row=0,column=0)
        
        self.btnDisplayData = Button(ButtonFrame, text="Display",  font=('arial',20,'bold'), width=11, height=1, bd=4, command=DisplayData)
        self.btnDisplayData.grid(row=0,column=1)
        
        self.btnClearData = Button(ButtonFrame, text="Clear",  font=('arial',20,'bold'), width=12, height=1, bd=4,command=clearData)
        self.btnClearData.grid(row=0,column=2)
        
        self.btnDeleteData = Button(ButtonFrame, text="Delete",  font=('arial',20,'bold'), width=11, height=1, bd=4, command=DeleteData)
        self.btnDeleteData.grid(row=0,column=3)
        
        self.btnSearchData = Button(ButtonFrame, text="Search",  font=('arial',20,'bold'), width=12, height=1, bd=4,command=searchDatabase)
        self.btnSearchData.grid(row=0,column=4)
        
        self.btnUpdateData = Button(ButtonFrame, text="Update",  font=('arial',20,'bold'), width=11, height=1, bd=4, command=update)
        self.btnUpdateData.grid(row=0,column=5)

        self.btnExit=Button(ButtonFrame, text="Exit", font=('arial',20,'bold'), height=1, width=12, bd=4, command=iExit)
        self.btnExit.grid(row=0,column=6)
        

            
        self.lblPID=Label(DataFrame1, font=('arial',14,'bold'), text="Patient ID", bg="papayawhip",padx=1, pady=2)
        self.lblPID.grid(row=0, column=0, sticky=W)
        self.txtPID=Entry(DataFrame1, font=('arial',14,'bold'),textvariable=PID, width=80)
        self.txtPID.grid(row=0,column=1)

        self.lblna=Label(DataFrame1, font=('arial',14,'bold'), text="Name:", bg="papayawhip",padx=1, pady=2)
        self.lblna.grid(row=1, column=0, sticky=W)
        self.txtna=Entry(DataFrame1, font=('arial',14,'bold'),textvariable=Name, width=80)
        self.txtna.grid(row=1,column=1)

        self.lblDOB=Label(DataFrame1, font=('arial',14,'bold'), text="Date Of Birth:", bg="papayawhip",padx=1, pady=2)
        self.lblDOB.grid(row=2, column=0, sticky=W)
        self.txtDOB=Entry(DataFrame1, font=('arial',14,'bold'),textvariable=DOB, width=80)
        self.txtDOB.grid(row=2,column=1)

        self.lblSex=Label(DataFrame1, font=('arial',14,'bold'), text="Sex:", bg="papayawhip",padx=1, pady=2)
        self.lblSex.grid(row=3, column=0, sticky=W)
        self.txtSex=Entry(DataFrame1, font=('arial',14,'bold'),textvariable=Sex, width=80)
        self.txtSex.grid(row=3,column=1)

        self.lblBloodgroup=Label(DataFrame1, font=('arial',14,'bold'), text="Blood Group:", bg="papayawhip",padx=1, pady=2)
        self.lblBloodgroup.grid(row=4, column=0, sticky=W)
        self.txtBloodgroup=Entry(DataFrame1, font=('arial',14,'bold'),textvariable=Bloodgroup, width=80)
        self.txtBloodgroup.grid(row=4,column=1)

        self.lblAdr=Label(DataFrame1, font=('arial',14,'bold'), text="Address:", bg="papayawhip",padx=1, pady=2)
        self.lblAdr.grid(row=5, column=0, sticky=W)
        self.txtAdr=Entry(DataFrame1, font=('arial',14,'bold'),textvariable=Address, width=80)
        self.txtAdr.grid(row=5,column=1)

        self.lblMobile=Label(DataFrame1, font=('arial',14,'bold'), text="Mobile:", bg="papayawhip",padx=1, pady=2)
        self.lblMobile.grid(row=6, column=0, sticky=W)
        self.txtMobile=Entry(DataFrame1, font=('arial',14,'bold'),textvariable=Mobile, width=80)
        self.txtMobile.grid(row=6,column=1)

        self.lblCash=Label(DataFrame1, font=('arial',14,'bold'), text="Cash paid:", bg="papayawhip",padx=1, pady=2)
        self.lblCash.grid(row=7, column=0, sticky=W)
        self.txtCash=Entry(DataFrame1, font=('arial',14,'bold'),textvariable=Cash, width=80)
        self.txtCash.grid(row=7,column=1)
                                   
                                   
                                   
                                   
                                   
