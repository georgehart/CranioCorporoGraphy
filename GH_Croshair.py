''' ------------------------------------------------------------------------------------------------------------------

Project     : TFE CranioCorpoGraphy
Author:     : Georges Hart
Date        : November 2019

Students    : Chafiq, Ilias


------------------------------------------------------------------------------------------------------------------ '''
import cv2
import sys
import numpy as np
import time


# ----- variables -----
a=0


calibration_distance = 0

resolutie_h = 640
resolutie_v = 480
box = 80
thickstep=20
thick = 5
crosshair_color = (200, 200, 200)


# ----- functions -----
def nothing(x):
    pass

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ',y)
    elif event ==cv2.EVENT_LBUTTONDOWN and flags == cv2.EVENT_FLAG_SHIFTKEY:
        crosshair(0,0)

# Crosshair in image

def crosshair(x,y):
    cv2.line(gray, (10, int(y/2)), (x-10,int(y/2)), crosshair_color , 1)  # vertical

    for h in range(int(x/2),0, -thickstep):
        cv2.line(gray, (h, (int(y/2)-thick)), (h, (int(y/2)+thick)), crosshair_color, 1)  # vertical

    for h in range(int(x/2),(int(x)), thickstep):
        cv2.line(gray, (h, (int(y / 2) - thick)), (h, (int(y / 2) + thick)), crosshair_color, 1)  # vertical

    cv2.line(gray, (int(x / 2), 10), (int(x / 2), y-10), crosshair_color, 1)  # vertical
    for v in range(int(y/2), int(y), thickstep):
        cv2.line(gray, ((int(x/2)-thick),v), ((int(x/2)+thick),v), crosshair_color, 1)  # horizontal
    for v in range(int(y/2), 0, -thickstep):
        cv2.line(gray, ((int(x/2)-thick),v), ((int(x/2)+thick),v), crosshair_color, 1)  # horizontal

    # Box center
    # cv2.rectangle(gray, (int(x/2) - box, int(y/2) - box), (int(x/2) + box, int(y/2) + box), crosshair_color, 1)

    # Box center
    for x in range(0,(int(box/2)*6),int(box/2)):
        cv2.circle(gray,(int(resolutie_h/2),int(resolutie_v/2)),x,crosshair_color,1)

    # text in video
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(gray, 'TFE2020 - CranioCorporoGraphy', (5, 25), font, 0.4, (255, 255, 255), 1, cv2.LINE_AA)



# create an video object
video = cv2.VideoCapture(0)
video.set(3,resolutie_h)
video.set(4,resolutie_v)


while True:

    a=a+1
    # create frame object
    check, frame = video.read()

    # print (check)
    # print(frame) # representing image





    # converting image to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # show the frame
    cv2.imshow("TFE CranioCorporoGraphy - 2020",frame)

    crosshair(resolutie_h, resolutie_v)
    cv2.createTrackbar("test", "gray", 50, 500, nothing)
    cv2.imshow("Analysis",gray)

    # Mouse events
    cv2.setMouseCallback("Analysis",click_event)



    # Press any Key to out (miliseconds)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print(a)

# ----- shutdown the camera -----
video.release()
cv2.destroyAllWindows()

''' ----- BIBLIOGRAPHY -----


'''
