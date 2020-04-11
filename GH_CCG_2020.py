''' ===================================================================

Project         : CranioCorporoGraphy
Author          : Georges Hart
Date            : november 2019

File            : GH_CCG_2020.py
Version         : 0.11 - 11 april'20   :-)
GitHub          :


Description     :





======================================================================= '''



# ----- Import libraries -----

import cv2
import numpy as np

# -----Definitions -----

font = cv2.FONT_HERSHEY_COMPLEX

# ----- Functions -----

def nothing(x):
    pass


# ----- Capture Video camera -----

cap =cv2.VideoCapture(0)


# ----- MASK Tool -----
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H", "Trackbars", 150, 180, nothing)
cv2.createTrackbar("L-S", "Trackbars", 100, 250, nothing)
cv2.createTrackbar("L-V", "Trackbars", 10, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 180, 180, nothing)
cv2.createTrackbar("U-S", "Trackbars", 220, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 255, 255, nothing)

while True:
    _, frame =cap.read()
    # ----- HSV convertie -----
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # HSV converter

    #----- MASK TOOL -----

    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")

    lower_color = np.array([l_h, l_s, l_v])
    uper_color = np.array([u_h, u_s, u_v])

    # ----- Mask -----
    mask = cv2.inRange(hsv, lower_color, uper_color)

    # ---- Cleaning small parts with black for pixels bigger thnpixels 5x5
    kernel = np.ones((10, 10), np.uint8)
    mask = cv2.erode(mask, kernel)

    # ----- Contour detection -----
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # -----

    for cnt in contours:
        # ----- AREA FILTER ----
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 100:
            cv2.drawContours(frame, [approx], 0, (255, 255, 0), 2)
        '''
        if len(approx) == 3:
            cv2.putText(frame, "Triangle", (x, y), font, 0.5, (0, 0, 0))
        elif len(approx) == 4:
            cv2.putText(frame, "Rectangle", (x, y), font, 0.5, (0, 0, 0))
        '''
        if 20< len(approx) < 30:
            cv2.putText(frame, str(x) + ' - ' + str(y) , (x+10, y-10), font, 0.5, (255, 255, 255))


    cv2.imshow("Frame", frame)
    cv2.imshow("Mask",mask)


    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



"""
Sources:

Youtube         : https://www.youtube.com/watch?v=AMFhjir4WgQ
Pysource        : https://pysource.com/2018/12/29/real-time-shape-detection-opencv-with-python-3/

"""


