from PIL import ImageTk, Image
import datetime
import tkinter as tk
from tkinter import StringVar, messagebox, Canvas, Frame, BOTH, NW
import Button as bt
from ThongKe import *
class Login(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(width=350)
        self.config(height=500)
        self.config(background="#1c2341")
        self.back = bt.Button(self,r"E:\C++ VS\jbdc\jbdc\NHANDIEN\image\left.png","",50,50)
        self.back.place(x = 10, y = 10)
        label3 = tk.Label(self, text = "Đăng nhập", fg = "#6DFFE7", bg= "#1C2341", font = ("Aria",24,"bold"))
        label3.place(x = 95,y = 143)
        label4 = tk.Label(self, text = "User", fg = "#6DFFE7", bg= "#1C2341", font = ("Aria",18,"bold"))
        label4.place(x = 30,y = 194)
        label5 = tk.Label(self, text = "Password", fg = "#6DFFE7", bg= "#1C2341", font = ("Aria",18,"bold"))
        label5.place(x = 30,y = 273)
        label6 = tk.Label(self, text = "Forgot password?", fg = "#FFFFFF", bg= "#1C2341", font = ("Aria",10,"bold"))
        label6.place(x = 120,y = 417)
        self.variable1 = StringVar() # Value saved here
        self.variable2 = StringVar()
        user = tk.Entry(self, width = 21, bg = "#394F6B", textvariable=self.variable1, font = ("Aria",18,"bold"),foreground="#ffffff")
        user.place(x = 36, y = 235)
        passw = tk.Entry(self, width = 21, bg = "#394F6B", textvariable=self.variable2, show='*', font = ("Aria",18,"bold"),foreground="#ffffff")
        passw.place(x = 36, y = 313)
		#bts = tk.Button(self, text='Show Pass', command = self.showpass)
		#bts.place(x = 140, y = 360)
        self.btLogin = tk.Button(self, text = "Đăng Nhập", width = "13", fg = "#1C2341", bg = "#6DFFE7", pady = 2, font = ("Aria",16,"bold"))
        self.btLogin.place(x = 91, y = 367)
        self.canvas2 = Canvas(self ,width = 100, height = 100, bg= "#1c2341", highlightthickness =0)    
        img= (Image.open(r"E:\C++ VS\jbdc\jbdc\NHANDIEN\image\user.png"))
        resized_image= img.resize((70,70), Image.ANTIALIAS)
        self.new_image= ImageTk.PhotoImage(resized_image)
        self.canvas2.create_image(10, 10, anchor=NW, image = self.new_image) 
        self.canvas2.place(x = 125,y = 40)

        