from App import *
from Staff import *
from ThongKe import *
from MyNoteBook import *
from Home import *
from Login import *
import tkinter as tk
root = tk.Tk()
home = FormLogin(root)
app = App(root,805,500)
def runApp():
    home.pack()
def toApp():
        home.pack_forget()
        def toHome():
            app.pack_forget()
            home.toHome()
            home.login.variable1.set("")
            home.login.variable2.set("")
            home.pack()
        app.nav.buttons[-1].config(command = toHome)
        app.pack()

home.login.btLogin.config(command=toApp)
runApp()
root.mainloop()
