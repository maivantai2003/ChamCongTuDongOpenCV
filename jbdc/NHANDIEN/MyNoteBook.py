import tkinter as tk
from Login import Login
from Home import Home
class MyNoteBook(tk.Frame):
    def __init__(self, master, width, height, tdx, tdy ) -> None:
        super().__init__(master)
        self.config(width = width)
        self.config(height = height)
        self.place(x = tdx, y = tdy)
        self.Navigation = tk.Frame(self,width = 105, height = height, bg="#1c2341")
        self.Navigation.place(x = 0, y = 0)
        self.place(x = 0, y = 0)
        self.tabs = []
        self.buttons = []
        self.currentTab = None
    def Out(self):
        self.master.quit()
    def addTab(self,tab,name,image):
        self.tabs.append(tab)
        self.buttons.append(0)
        self.buttons[-1] = tk.Button(self.Navigation,image = image,text=name,width=80,height = 100, compound=tk.TOP,background="#1c2341",relief=tk.FLAT,font=("Arial",12,"bold"),command=lambda:self.showTab(tab),foreground="#ffffff")
        self.buttons[-1].place(x = 10, y = 10 +110*(len(self.tabs) - 1))
        if self.currentTab is None:
            self.currentTab = self.tabs[0]

    def showTab(self, tab):
        self.currentTab.pack_forget()
        tab.pack()
        self.currentTab = tab






    


