import cv2
import numpy as np
def rectContour(contours):
    rectCon = []
    for i in contours:
        area = cv2.contourArea(i)
        #print(area)
        if area > 80:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)

            if len(approx) == 4:
                rectCon.append(i)
    rectCon = sorted(rectCon, key=cv2.contourArea, reverse=True)
    return rectCon
def getCornerPoints(cont):
    peri = cv2.arcLength(cont, True) # LENGTH OF CONTOUR
    approx = cv2.approxPolyDP(cont, 0.02 * peri, True) # APPROXIMATE THE POLY TO GET CORNER POINTS
    return approx
def reorder(myPoints):

    myPoints = myPoints.reshape((4, 2)) # REMOVE EXTRA BRACKET
    #print(myPoints)
    myPointsNew = np.zeros((4, 1, 2), np.int32) # NEW MATRIX WITH ARRANGED POINTS
    add = myPoints.sum(1)
    #print(add)
    #print(np.argmax(add))
    myPointsNew[0] = myPoints[np.argmin(add)]  #[0,0]
    myPointsNew[3] =myPoints[np.argmax(add)]   #[w,h]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] =myPoints[np.argmin(diff)]  #[w,0]
    myPointsNew[2] = myPoints[np.argmax(diff)] #[h,0]

    return myPointsNew

def splitBoxes(img):
    rows = np.vsplit(img, 20)
    #cv2.imshow("splitBoxes", rows[19])
    boxes = []
    for r in rows:
        cols = np.hsplit(r, 20)
        for box in cols:
            boxes.append(box)
    #cv2.imshow("splitBoxes", box)
    return boxes
def showAnswers(img,myIndex,grading,ans,questions,choices):
    secW = int(img.shape[1] / questions)
    secH = int(img.shape[0] / choices)
    col=0
    row=0
    numc=0
    for x in range(0, 80):
        myAns = myIndex[x]

        col=col+1
        if(col==1):
            row=row+1
            numc=row
            cX = (myAns * secW) + secW // 2
            cY = ((numc - 1) * secH) + secH // 2
        elif (col==2):
            numc=row+20
            myAns=myAns+ 5
            cX = (myAns * secW) + secW // 2
            cY = ((row - 1) * secH) + secH // 2
        elif (col == 3):
            numc=row+40
            myAns = myAns + 10
            cX = (myAns * secW) + secW // 2
            cY = ((row - 1) * secH) + secH // 2
        elif (col == 4):
            numc = row + 60
            myAns = myAns + 15
            cX = (myAns * secW) + secW // 2
            cY = ((row - 1) * secH) + secH // 2
            col=0
        #print("col", col)

        cv2.circle(img, (cX, cY), 8, (0,255,0), cv2.FILLED)
        #print("col", x," X=",cX," Y=",cY)
    return img
