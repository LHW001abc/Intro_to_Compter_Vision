import numpy as np
import cv2 as cv

def print(x):
    print(x)    

while(True):
    frame = cv.imread('C:/Users/pc/Desktop/Computer_Vision/Intro_to_Compter_Vision/image.png')
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_b = np.array([110,50,50])
    u_b = np.array([130,255,255])

    mask = cv.inRange(hsv, l_b, u_b) #thresholding the hsv image to get only blue colors
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)


    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break


cv.destroyAllWindows()
