from datetime import datetime
import pyodbc as po
import pandas as pd
from ThongBaoChamCong import *
connection=po.connect(driver='{ODBC Driver 17 for SQL Server}',host='MSI\SQLEXPRESS',database='SGU',trusted_connection='yes')
def InsertData(manv,hoten,chucvu):
    cur=connection.cursor()
    cur.execute("insert tbNhanVien values(?,?,?)",manv,hoten,chucvu)
    cur.commit()
def DeleteData(manv):
    cur=connection.cursor()
    cur.execute("delete tbNhanVien where Manv=?",manv)
    cur.commit()
def UpdateData(manv,hoten,chucvu):
    cur=connection.cursor()
    cur.execute("update tbNhanVien set Hoten=?,Chucvu=? where Manv=?",hoten,chucvu,manv)
    cur.commit()
def getData():
    cur=connection.cursor()
    cur.execute("select * from tbNhanVien")
    temp=cur.fetchall()
    return temp
def getDataDict():
    cursor=connection.cursor()
    cursor.execute("select Manv,Hoten from tbNhanVien")
    temp=cursor.fetchall()
    t=dict(temp)
    tmp={}
    for key,item in t.items():
        tmp[int(key)]=item
    return tmp
def ExportExcel():
    curson=connection.cursor()
    curson.execute("select * from tbNhanVien,tbChamCong where tbNhanVien.Manv=tbChamCong.Manv order by tbChamCong.Ngay ASC")
    temp=curson.fetchall()
    t1=[]
    t2=[]
    t3=[]
    t4=[]
    t5=[]
    t6=[]
    for i in temp:
        t1.append(i[0])
        t2.append(i[1])
        t3.append(i[2])
        t4.append(i[4])
        t5.append(i[5])
        t6.append(i[6])
    print(t1,t2,t3,t4,t5,t6)
    df=pd.DataFrame({"Mã Nhân Viên":t1,"Tên Nhân Viên":t2,"Chức Vụ":t3,"Ngày":t4,"Thời Gian Vào":t5,"Thời Gian Ra":t6})
    timecheck=datetime.now().strftime('%d_%m_%Y')
    filename="chamcong_"+timecheck+".xlsx"
    print(filename)
    df.to_excel(filename,index=False)
def getChamCong():
    cur=connection.cursor()
    cur.execute("select * from tbChamCong")
    temp=cur.fetchall()
    return temp
def getName(manv):
    cur=connection.cursor()
    cur.execute("select Hoten from tbNhanVien where Manv=?",manv)
    temp=cur.fetchall()
    return temp[0][0]
def checkInAndOut(manv,timecheck):
    t=timecheck.split("_")
    curson=connection.cursor()
    curson.execute("select * from tbChamCong where Manv=? and Ngay=?",manv,t[0])
    temp=curson.fetchall()
    print(temp)
    if(temp==[]):
       curson.execute("insert tbChamCong values(?,?,?,?)",manv,t[0],t[1],"")
       curson.commit()
       ThongBao(timecheck,manv,getName(manv),"Đã Chấm Công Vào",r"E:\C++ VS\jbdc\ChamCongVao.mp3")
    if(temp!=[]):
        curson.execute("select GioVao,GioRa from tbChamCong where Manv=? and Ngay=?",manv,t[0])
        thoigian=curson.fetchall()
        if(thoigian[0][0]!='' and thoigian[0][1]==''):
             curson.execute("update tbChamCong set GioRa=? where Manv=? and Ngay=?",t[1],manv,t[0])
             curson.commit()
             ThongBao(timecheck,manv,getName(manv),"Đã Chấm Công Ra",r"E:\C++ VS\jbdc\ChamCongRa.mp3")
        elif (thoigian[0][0]!='' and thoigian[0][1]!=''):
             ThongBao(timecheck,manv,getName(manv),"Đã Hoành Thành Chấm Công Trong Ngày",r"E:\C++ VS\jbdc\HoanThanh.mp3")
            