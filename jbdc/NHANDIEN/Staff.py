import tkinter as tk
from tkinter import StringVar, ttk
from PIL import Image, ImageTk
from opencv1 import *
from opencv2 import *
from opencv3 import *
from Database import *
class Staff(tk.Frame):
    def __init__(self, master, background, width, height, tdx, tdy) -> None:
        super().__init__(master)
        self.config(background = background)
        self.config(width = width)
        self.config(height = height)
        self.pack()
        thongTinNVTxt = tk.Label(self, text="Thông tin nhân viên", font=("Arial", 20, "bold"), foreground="#000000", background="#ffffff")
        thongTinNVTxt.place(x=12, y=13)
        IDTxt = tk.Label(self, text="ID", font=("Arial", 20, "bold"),
                        foreground="#000000", background="#ffffff")
        IDTxt.place(x=34, y=51)

        hoTenTxt = tk.Label(self, text="Họ và tên", font=(
            "Arial", 20, "bold"), foreground="#000000", background="#ffffff")
        hoTenTxt.place(x=180, y=51)

        chucVuTxt = tk.Label(self, text="Chức vụ", font=(
            "Arial", 20, "bold"), foreground="#000000", background="#ffffff")
        chucVuTxt.place(x=385, y=51)
        self.IDValue = StringVar()
        self.HoTenValue = StringVar()
        self.ChucVuValue = StringVar()
        IDFlied = tk.Entry(self, width=10, background="#394f6b",
                        foreground="#ffffff", font=("Arial", 14, "bold"),textvariable=self.IDValue)
        IDFlied.place(x=34, y=85)

        HoTenFlied = tk.Entry(self, width=15, background="#394f6b",
                            foreground="#ffffff", font=("Arial", 14, "bold"),textvariable=self.HoTenValue)
        HoTenFlied.place(x=180, y=85)

        chucVuFlied = tk.Entry(self, width=15, background="#394f6b",
                            foreground="#ffffff", font=("Arial", 14, "bold"),textvariable=self.ChucVuValue)
        chucVuFlied.place(x=385, y=85)
        
        line = tk.Frame(self,background="#1C2341", width = 660, height = 2)
        line.place(x = 27, y= 200)

        danhSachNVTxt = tk.Label(self,text = "Danh sách nhân viên",font=("Arial", 20, "bold"), foreground="#000000", background="#ffffff")
        danhSachNVTxt.place(x=12,y=210)

        self.danhSachNV = ttk.Treeview(self)
        self.danhSachNV["columns"] = ("ID","Name","Position")
        self.danhSachNV.column("#0",width=0,stretch=tk.NO)
        self.danhSachNV.column("ID",width=200, anchor=tk.CENTER)
        self.danhSachNV.column("Name",width=250, anchor=tk.CENTER)
        self.danhSachNV.column("Position",width=230, anchor=tk.CENTER)
        self.danhSachNV.heading("ID",text = "ID")
        self.danhSachNV.heading("Name",text = "Họ và tên")
        self.danhSachNV.heading("Position",text = "Chức Vụ")
        self.danhSachNV.place(x=12,y=250)
        self.insertTreeView()
        icon = tk.PhotoImage(file=r"E:\C++ VS\jbdc\jbdc\NHANDIEN\image\scan.png")
        new_width = 50
        new_height = 50
        self.image = icon.subsample(round(icon.width() / new_width), round(icon.height() / new_height))
        self.nhanDang = tk.Button(self,image = self.image, relief="flat", command=self.addFace)
        self.nhanDang.place(x=580, y=53)
        them = tk.Button(self,text="Thêm",font=("Arial",16,"bold"),background="#1C2341",foreground="#FF7A00",width=5,command=self.addNV)
        them.place(x = 34, y = 135)
        sua = tk.Button(self,text="Sửa",font=("Arial",16,"bold"),background="#1C2341",foreground="#FF7A00", width=5, command=self.changeNV)
        sua.place(x = 134, y = 135)
        xoa = tk.Button(self,text="Xóa",font=("Arial",16,"bold"),background="#1C2341",foreground="#FF7A00", width=5, command=self.delNV)
        xoa.place(x = 234, y = 135)
        reset=tk.Button(self,text="X",background="#1C2341",foreground="#FF7A00", width=5,command=self.ClearText)
        reset.place(x = 334, y = 135)
        def clickInTree(event):
         for i in self.danhSachNV.selection():
           item=self.danhSachNV.item(i)
           print(item)
           recond=item['values']
           self.IDValue.set(recond[0])
           self.HoTenValue.set(recond[1])
           self.ChucVuValue.set(recond[2])
        self.danhSachNV.bind('<<TreeviewSelect>>',clickInTree)
    def insertTreeView(self):
        self.danhSachNV.delete(*self.danhSachNV.get_children())
        temp=getData()
        for i in temp:
            i=list(i)
            self.danhSachNV.insert("","end",value=i)
    def addNV(self):
        if self.IDValue.get() == "" or self.HoTenValue.get()=="" or self.ChucVuValue.get()=="":
            tk.messagebox.showinfo("Thông báo", "Vui lòng điền đầy đủ thông tin")
        else:
            InsertData(self.IDValue.get(),self.HoTenValue.get(),self.ChucVuValue.get())
            self.insertTreeView()
            FaceInFor(self.IDValue.get())
            TrainingData()
            self.ClearText()
            tk.messagebox.showinfo("Thông báo", "Thêm thành công")
            ''''else:
                tk.messagebox.showinfo("Thông báo", "Mã nhân viên đã tônf tại")'''
    def changeNV(self):
        if tk.messagebox.askquestion("Xác nhận", "Bạn có muốn thay đổi thông tin?") == "yes":
            UpdateData(self.IDValue.get(),self.HoTenValue.get(),self.ChucVuValue.get())
            self.ClearText()
            self.insertTreeView()
    def delNV(self):
        if tk.messagebox.askquestion("Xác nhận", "Bạn có muốn xóa?") == "yes":
            DeleteData(self.IDValue.get())
            self.ClearText()
            self.insertTreeView()
    def addFace(self):
        TrainingData()
    def ClearText(self):
        self.IDValue.set("")
        self.HoTenValue.set("")
        self.ChucVuValue.set("")