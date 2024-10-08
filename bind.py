import numpy as np
import cv2 as cv    

def print(x):
    print(x)

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')

cv.createTrackbar('B','image',0,255,print)
cv.createTrackbar('G','image',0,255,print)
cv.createTrackbar('R','image',0,255,print)
switch = '0 : OFF \n1 : ON' 
cv.createTrackbar(switch, 'image',0,1,print)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    b = cv.getTrackbarPos('B','image')
    g = cv.getTrackbarPos('G','image')
    r = cv.getTrackbarPos('R','image')
    s = cv.getTrackbarPos(switch,'image')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv.destroyAllWindows()
