import cv2
import numpy as np

vid = cv2.VideoCapture(0)
while(1):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


#BLUE
#  lower_range = np.array([100,100,100])
#  upper_range = np.array([140,255,255])



#RED 

  lower_range = np.array([150,100,100])
  upper_range = np.array([180,220,255])
  

  mask = cv2.inRange(hsv,lower_range,upper_range)
  res = cv2.bitwise_and(image,image, mask= mask) 

  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 10)
 
  # ensure at least some circles were found
  if circles is not None:
    print ("circles")
    # convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")
 
    # loop over the (x, y) coordinates and radius of the circles
    for (x, y, r) in circles:
      # draw the circle in the output image, then draw a rectangle
      # corresponding to the center of the circle
      cv2.circle(image, (x, y), r, (0, 255, 0), 2)
      cv2.rectangle(image, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
      print (" x:{} y:{} ".format(x, y) )


  cv2.imshow('image_window_name',image)
  cv2.imshow('mask_window_namw',mask)
  
  if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
cv2.destroyAllWindows()
