import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from Button import *
from Database import getChamCong,ExportExcel
class ThongKe(tk.Frame):
    def __init__(self, master, width, height) -> None:
        super().__init__(master)
        self.config(width = width)
        self.config(height = height)
        self.config(background="#ffffff")
        self.pack()
        lichSuChamCongTxt = tk.Label(self,text="Lịch sử chấm công",font=("Arial",20,"bold"),background="#ffffff", foreground="#000000")
        lichSuChamCongTxt.place(x = 19, y= 13)
        tuTxt = tk.Label(self,text="Từ",font=("Arial",16,"bold"),background="#ffffff", foreground="#000000")
        tuTxt.place(x = 26, y= 54)
        denTxt = tk.Label(self,text="Đến",font=("Arial",16,"bold"),background="#ffffff", foreground="#000000")
        denTxt.place(x = 207, y= 54)
        nhanVienTxt = tk.Label(self,text="NV",font=("Arial",16,"bold"),background="#ffffff", foreground="#000000")
        nhanVienTxt.place(x = 398, y= 54)
        btnLoad=tk.Button(self,text='LOAD',command=self.load,bg='red')
        btnLoad.place(x=290,y=25)
        self.IDValue = StringVar()
        self.fromDate = DateEntry(self,width = 15)
        self.fromDate.place(x = 65,y = 56)
        self.toDate = DateEntry(self,width = 15)
        self.toDate.place(x = 255,y = 56)
        self.NVField = tk.Entry(self,width = 15,bg="#394F6B",font=("Arial",14,"bold"),foreground="#ffffff",textvariable=self.IDValue)
        self.NVField.place(x =440 , y = 52)
        icon = tk.PhotoImage(file=r"E:\C++ VS\jbdc\jbdc\NHANDIEN\image\funnel.png")
        new_width = 30
        new_height = 30
        self.image = icon.subsample(round(icon.width() / new_width), round(icon.height() / new_height))
        
        def handle(event):
            self.filter_()
        self.filter = tk.Button(self,image = self.image,bg="#ffffff", relief=tk.FLAT,command=self.filter_)
        self.filter.place(x = 635, y = 45)
        # self.NVField.bind("<KeyRelease>", handle)
        self.detached_items = []
        self.danhSachChamCong = ttk.Treeview(self)
        self.danhSachChamCong["columns"] = ("ID","Ngay","GioVao","GioRa")
        self.danhSachChamCong.column("#0",width=0,stretch=tk.NO)
        self.danhSachChamCong.column("ID",width=150, anchor=tk.CENTER)
        self.danhSachChamCong.column("Ngay",width=250, anchor=tk.CENTER)
        self.danhSachChamCong.column("GioVao",width=150, anchor=tk.CENTER)
        self.danhSachChamCong.column("GioRa",width=150, anchor=tk.CENTER)
        self.danhSachChamCong.heading("ID",text = "ID")
        self.danhSachChamCong.heading("Ngay",text = "Ngày")
        self.danhSachChamCong.heading("GioVao",text = "Giờ Vào")
        self.danhSachChamCong.heading("GioRa",text = "Giờ Ra")
        self.danhSachChamCong.place(x=12,y=100)
        self.insertTreeView()
        self.exportEx = Button(self,r"E:\C++ VS\jbdc\jbdc\NHANDIEN\image\excel.png","",50,50)
        self.exportEx.config(command=self.exportExcel)
        self.exportEx.place(x =600 , y =330 )
        self.exportEx.config(bg="#ffffff")
        exportTxt = tk.Label(self,text="Export Excel",font={"Arial",14,"bold"},bg="#ffffff")
        exportTxt.place(x = 570,y = 380)
    def exportExcel(self):
        if tk.messagebox.askquestion("Xác nhận", "Bạn có xuất file excel ?") == "yes":
           ExportExcel()
    def insertTreeView(self):
        self.danhSachChamCong.delete(*self.danhSachChamCong.get_children())
        temp=getChamCong()
        for i in temp:
            i=list(i)
            self.danhSachChamCong.insert("","end",value=i)
    def load(self):
        self.insertTreeView()
    def filter_(self):
        self.undetact()
        if self.IDValue.get() != "":
            ds = getChamCong()
            for x,item in enumerate(self.danhSachChamCong.get_children()):
                manv = ds[x][0]
                if manv != self.IDValue.get():
                    self.danhSachChamCong.detach(item)
                    self.detached_items.append(item)
    def undetact(self):      
        for i in self.detached_items:
            self.danhSachChamCong.reattach(i,'',0)
        self.detached_items.clear()
if __name__=="__main__":
    pass
    
