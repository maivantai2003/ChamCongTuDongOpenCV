import cv2
import numpy as np
import pandas as pd
import time
import os
from datetime import datetime
import time
from Database import getDataDict,checkInAndOut,getName
def ResultData():
 recognizer=cv2.face.LBPHFaceRecognizer_create()
 recognizer.read(r"E:\C++ VS\jbdc\jbdc\trainer/trainer.yml")
 faceCasade=cv2.CascadeClassifier(r"E:\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")
 font=cv2.FONT_HERSHEY_SIMPLEX
 manv=0
 cam=cv2.VideoCapture(0)
 cam.set(3,840)
 cam.set(4,680)
 minW=0.1*cam.get(3)
 minH=0.1*cam.get(4)
 count=0
 exit=False
 while True:
    _,img=cam.read()
    img=cv2.flip(img,1)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #faces=faceCasade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(int(minW),int(minH)))
    faces=faceCasade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        manv,confidence=recognizer.predict(gray[y:y+h,x:x+w])
        t=manv
        if(confidence<35):
            manv=getName(manv)
            confidence="{0}%".format(round(100 - confidence))
            count+=1
            print(count)
            if(count==15):
                cv2.waitKey(2000)  
                timecheck=datetime.now().strftime('%d/%m/%Y_%H:%M:%S')
                checkInAndOut(t,timecheck)
                count=0
                #exit=1             
        else:
            manv="unknow"
            count=0
            confidence="{0}%".format(round(100 - confidence))
        cv2.putText(img,str(manv),(x+5,y-5),font,1,(255,255,25),2)
        cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(255,255,0),1)
    cv2.imshow("Chấm Công",img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
    if(exit==1):
        break
 cam.release()
 cv2.destroyAllWindows()
