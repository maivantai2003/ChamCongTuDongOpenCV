import tkinter as tk
from tkinter import Label, messagebox
from playsound import playsound
def ThongBao(thoigian,manv,tennv,txt,amthanh):
    root = tk.Tk()
    width = 400
    height = 400
    t1 = root.winfo_screenwidth()
    t2 = root.winfo_screenheight()
    x = (t1//2) - (width // 2)
    y = (t2//2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    txtHienThi=tk.Label(root,text=txt,font=("Helvetica", 15),fg='blue').pack(side='top')
    txtThongTin=tk.Label(root,text="Thời Gian: "+str(thoigian)+"\nMã Nhân Viên: "+str(manv)+"\nTên Nhân Viên:"+str(tennv),font=("Helvetica", 15),fg='red').place(x=75,y=50)
    playsound(amthanh)
    def close_window():
         root.destroy()
    root.after(500, close_window)
if __name__=="__main__":
    pass