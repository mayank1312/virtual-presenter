import os
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

width, height = 1280, 720
folderPath = "Presentation"
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

pathImages = sorted(os.listdir(folderPath), key=lambda x: int(x.split('.')[0]))

imgNumber = 0
hs, ws = int(120 * 2), int(213 * 2)
gestureThreshold = 530
buttonPressed = False
buttonCounter = 0
buttonDelay = 30
annotations=[]  # <-- THIS IS THE FIX
annotationNumber=-1
annotationStart=False

frameRx = 400
frameRy = 200

detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    pathFullImg = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImg)
    h, w, _ = imgCurrent.shape

    cv2.rectangle(img, (width-frameRx, frameRy), (width, height - frameRy), (0, 255, 0), 2)
    hands, img = detector.findHands(img)


    if hands and buttonPressed is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx, cy = hand["center"]
        lmList = hand["lmList"]

        indexFingerX, indexFingerY = lmList[8][0], lmList[8][1]

        handX = np.clip(indexFingerX, width-frameRx, width )
        handY = np.clip(indexFingerY, frameRy, height - frameRy)

        xVal = int(np.interp(handX, [width-frameRx, width], [0, w]))
        yVal = int(np.interp(handY, [frameRy, height - frameRy], [0, h]))

        indexFinger = xVal, yVal

        if cy <= gestureThreshold:
            if fingers == [1, 0, 0, 0, 0]:
                if imgNumber > 0:
                    buttonPressed = True
                    annotations = [] # Reset annotations on slide change
                    annotationNumber = -1
                    annotationStart = False
                    imgNumber = imgNumber - 1

            if fingers == [0, 0, 0, 0, 1]:
                if imgNumber < len(pathImages) - 1:
                    buttonPressed = True
                    annotations = [] # Reset annotations on slide change
                    annotationNumber = -1
                    annotationStart = False
                    imgNumber = imgNumber + 1

        if fingers == [0, 1, 1, 0, 0]:
            cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)


        if fingers == [0, 1, 0, 0, 0]:
            if not annotationStart:
                annotationStart = True
                annotationNumber = annotationNumber + 1
                annotations.append([])
            cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
            annotations[annotationNumber].append(indexFinger)
        else:
            annotationStart = False

        if fingers == [0, 1, 1, 1, 0]:
            if annotations:
                annotations.pop(-1)
                annotationNumber = annotationNumber - 1
                buttonPressed = True

    if buttonPressed:
        buttonCounter += 1
        if buttonCounter > buttonDelay:
            buttonCounter = 0
            buttonPressed = False

    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
         if j != 0:
          cv2.line(imgCurrent,annotations[i][j-1],annotations[i][j],(0,0,200),12)

    imgSmall = cv2.resize(img, (ws, hs))
    imgCurrent[0:hs, w - ws:w] = imgSmall

    cv2.imshow('img', img)
    cv2.imshow('Sildes', imgCurrent)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()