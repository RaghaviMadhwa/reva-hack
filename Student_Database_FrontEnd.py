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
