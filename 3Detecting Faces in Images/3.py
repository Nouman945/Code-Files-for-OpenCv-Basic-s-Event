#import the libraries
import cv2
import numpy as np

#load the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# cv2.imread()

# To capture video from Webcam 
cap = cv2.VideoCapture(0)

while True:
    #read the image
    flag , img = cap.read()
    # print(flag)

    #Conveting to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #detect the faces
    faces = face_cascade.detectMultiScale(img,1.1,4)

    #Rectangle Boxes around the Faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img,(x,y), (x+w,y+h), (255,0,0),3)

    #Display Video
    cv2.imshow('img',img)

    # k = cv2.waitKey('q') & 0xff
    # if k==27:
    #     break
    
    k = cv2.waitKey(0)
    print(chr(k))
    if k == ord('q'):
        break


cap.release()
