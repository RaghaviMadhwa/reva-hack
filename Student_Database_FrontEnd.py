#Frontend

from tkinter import*
import tkinter.messagebox
import stdDatabase_BackEnd
import tkinter.ttk as ttk 


class Student:

    def __init__(self,root):
        self.root = root
        self.root.title("Patient Records System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="skyblue")
