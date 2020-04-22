import cv2
import numpy as np
import runSteering as rs
import face_recognition

runX = 18.1466
runY = 15.9733

startX = 90
startY = 90
rs.RunStreering(rs.XPin, startX)
rs.RunStreering(rs.YPin, startY)

faceImage = face_recognition.load_image_file('face.jpg')
faceData = face_recognition.face_encodings(faceImage)[0]
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
flag = True
while True:
    res, dstImg = cap.read()
    testImg = cv2.resize(dstImg, (0, 0), fx=0.25, fy=0.25)
    if flag:
        faceNames = []
        rgbTestImg = testImg[:, :, ::-1]
        faceLocations = face_recognition.face_locations(rgbTestImg)
        faceEncodings = face_recognition.face_encodings(rgbTestImg, faceLocations)
        for faceEncoding in faceEncodings:
            faceDistance = face_recognition.face_distance([faceData], faceEncoding)
            name = "UnKnown"
            if faceDistance < 0.5:
                name = "Lena Forsen"
            faceNames.append(name)
    flag = not flag
    for (top, right, bottom, left), name in zip(faceLocations, faceNames):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        medilY = (top + bottom) / 2
        medilX = (left + right) / 2
        if medilX < 213:
            xAngNum = startX - runX
        elif medilX > 426:
            xAngNum = startX + runX
        if xAngNum < 30 | xAngNum > 150:
            break
        if medilY < 160:
            yAngNum = startY + runY
        elif medilY > 320:
            yAngNum = startY - runY
        if yAngNum < 30 | yAngNum > 150:
            break
        
        cv2.rectangle(dstImg, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(dstImg, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(dstImg, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    cv2.imshow("catch", dstImg)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()