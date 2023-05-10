import tkinter as tk
from MyNoteBook import *
from Staff import *
from ThongKe import *
from FormLogin import *
from PIL import ImageTk, Image
import datetime
import tkinter as tk
from tkinter import StringVar, messagebox, Canvas, Frame, BOTH, NW

class App(tk.Frame):
    def __init__(self, master, width, height):
        super().__init__(master)
        self.config(width=width)
        self.config(height=height)
        self.funcs = tk.Frame(self, width=700, height=500)
        self.funcs.place(x=105, y=0)
        self.staff = Staff(self.funcs, "#ffffff", 700, 500, 0, 0)
        self.thongKe = ThongKe(self.funcs, 700, 500)
        self.nav = MyNoteBook(self, 105, 500, 0, 0)
        img = (Image.open(r"E:\C++ VS\jbdc\jbdc\NHANDIEN\image\search.png"))
        resized_image = img.resize((70, 70), Image.ANTIALIAS)
        self.new_image = ImageTk.PhotoImage(resized_image)
        img2 = (Image.open(r"E:\C++ VS\jbdc\jbdc\NHANDIEN\image\bar-chart.png"))
        resized_image2 = img2.resize((70, 70), Image.ANTIALIAS)
        self.new_image2 = ImageTk.PhotoImage(resized_image2)
        img3 = (Image.open(r"E:\C++ VS\jbdc\jbdc\NHANDIEN\image\left-arrow.png"))
        resized_image3 = img3.resize((70, 70), Image.ANTIALIAS)
        self.new_image3 = ImageTk.PhotoImage(resized_image3)
        self.nav.addTab(self.staff, "Danh sách", self.new_image)
        self.nav.addTab(self.thongKe, "Thống kê", self.new_image2)
        self.nav.addTab(self, "Thoát", image=self.new_image3)



