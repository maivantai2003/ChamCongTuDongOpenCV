import tkinter as tk
from Login import *
from Home import *
class FormLogin(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.login = Login(self)
        self.home = Home(self)
        self.home.pack()
        self.login.back.config(command=self.toHome)
        self.home.btLogin.config(command=self.toLogin)
    def toLogin(self):
        self.home.pack_forget()
        self.login.pack()
    def toHome(self):
        self.login.pack_forget()
        self.home.pack()