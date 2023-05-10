import tkinter as tk
import datetime
from PIL import ImageTk, Image
from tkinter.tix import IMAGETEXT
from opencv3 import *
from Login import Login

class Home(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(background="#1c2341")
        self.config(width=350)
        self.config(height=500)
        self.fun = None
        label1 = tk.Label(self, text = "Ứng dụng chấm công tự động", fg = "#6DFFE7", bg= "#1C2341", font = ("Aria",14,"bold"))
        label1.place(x = 29,y = 192)
        label2 = tk.Label(self, text = "và quản lý chấm công", fg = "#6DFFE7", bg= "#1C2341", font = ("Aria",14,"bold"))
        label2.place(x = 71,y = 218)
        self.btLogin = tk.Button(self, text = "Đăng Nhập", width = "16", fg = "#1C2341", bg = "#6DFFE7", pady = 5, font = ("Aria",16,"bold"))
        self.btLogin.place(x = 70,y = 277)
        arr=getDataDict()
        b2 = tk.Button(self, text = "Chấm Công", width = "16", fg = "#1C2341", bg = "#6DFFE7", pady = 5, font = ("Aria",16,"bold"),command=ResultData)
        b2.place(x = 70,y = 350)
        self.canvas = tk.Canvas(self ,width = 100, height = 100, bg= "#1C2341", highlightthickness =0)    
        img= (Image.open(r"E:\C++ VS\jbdc\jbdc\NHANDIEN\image\time.png"))
        resized_image= img.resize((85,86), Image.ANTIALIAS)
        self.new_image= ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(10, 10, anchor=tk.NW, image = self.new_image) 
        self.canvas.place(x = 130,y = 80)
        
        self.date = tk.Label(self,font=("Arial",16,"bold"),bg="#1c2341",foreground="#6DFFE7")
        self.time = tk.Label(self,font=("Arial",16,"bold"),bg="#1c2341",foreground="#6DFFE7")
        # self.update_time()
        self.time.place(x=10,y=10)
        self.date.place(x=10,y=35)
    def update_time(self):
        now = datetime.datetime.now()
        day = now.strftime("%d/%m/%Y")
        time = now.strftime("%H:%M:%S")
        self.date.config(text=day)
        self.time.config(text=time)
        self.after(1000,self.update_time)


