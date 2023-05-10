import cv2
def FaceInFor(manv):
 cam=cv2.VideoCapture(0)
 cam.set(3,640)
 cam.set(4,480)
 facedec=cv2.CascadeClassifier(r"E:\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")
 face_id=manv
 print("\nKhoi Tao Camera ...")
 count=0
 while(True):
    _,img=cam.read()
    img=cv2.flip(img,1)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=facedec.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        count=count+1
        cv2.imwrite(r"E:\C++ VS\jbdc\jbdc\FACE_RECOGNIZE/User."+str(face_id)+'.'+str(count)+'.jpg',gray[y:y+h,x:x+w])
        cv2.imshow('image',img) 
    if cv2.waitKey(100) & 0xff == ord('q'):
        break
    elif count >= 150:
         break
 print("\nThoat")
 cam.release()
 cv2.destroyAllWindows()
