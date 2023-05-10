import cv2
import numpy as np
import os
from PIL import Image
def TrainingData():
 path=r"E:\C++ VS\jbdc\jbdc\FACE_RECOGNIZE"
 recognizer=cv2.face.LBPHFaceRecognizer_create()
 detector=cv2.CascadeClassifier(r"E:\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")
 def getImages(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faceSamples=[]
    ids=[]
    for imagePath in imagePaths:
        Faceimg=Image.open(imagePath).convert('L')
        img_numpy=np.array(Faceimg,'uint8')
        ma=int(os.path.split(imagePath)[-1].split(".")[1])
        faceSamples.append(img_numpy)
        ids.append(ma)
    return faceSamples,ids

 print("[INFO] Dang training du lieu ...")
 faces,ids=getImages(path)
 recognizer.train(faces,np.array(ids))
 recognizer.save(r"E:\C++ VS\jbdc\jbdc\trainer/trainer.yml")
 print("{0} khuon mat duoc train. Thoat".format(len(np.unique(ids))))
