# -----------------------------------------------------------------
# opencv -> Simple camera capture
# 
# -----------------------------------------------------------------

import numpy as np
import cv2


# ----- Variables -----
window_name = 'CranioCorporoGraphy'




cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    
    ret, frame = cap.read()

    # ----- Gray image construction -----
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow(window_name,frame)
    cv2.imshow("Gray {}".format(window_name),gray)
    
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()