import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # define range of RED color in HSV - taske koffie
    
    lower_hsv = np.array([150,100,100])
    upper_hsv = np.array([180,225,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_hsv, upper_hsv)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('real time',frame)
    cv.imshow('mask',mask)
    cv.imshow('result',res)
    
    
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()