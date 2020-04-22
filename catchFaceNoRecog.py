import cv2
import numpy as np

faceCatch = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, dstImg = cap.read()
    grayImg = cv2.cvtColor(dstImg, cv2.COLOR_BGR2GRAY)
    faces = faceCatch.detectMultiScale(grayImg, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))
    flag1 = 0
    for (x,y,w,h) in faces:
        cv2.rectangle(dstImg,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = grayImg[y:y+h, x:x+w]
        roi_color = dstImg[y:y+h, x:x+w]
        flag1 += 1
    cv2.imshow("catchNoRecog", dstImg)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
 
cap.release()
cv2.destroyAllWindows()