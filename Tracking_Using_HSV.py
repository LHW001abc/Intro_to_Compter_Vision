import numpy as np
import cv2 as cv

def print(x):
    print(x)
#for the video capture
cap = cv.VideoCapture(0)

cv.namedWindow('image')
cv.createTrackbar('LH','image',0,255,print)  
cv.createTrackbar('LS','image',0,255,print)
cv.createTrackbar('LV','image',0,255,print)
cv.createTrackbar('UH','image',255,255,print)
cv.createTrackbar('US','image',255,255,print)
cv.createTrackbar('UV','image',255,255,print)


while(1):
    #frame = cv.imread('C:/Users/pc/Desktop/Computer_Vision/Intro_to_Compter_Vision/image.png')
    _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    lh = cv.getTrackbarPos('LH','image')
    ls = cv.getTrackbarPos('LS','image')
    lv = cv.getTrackbarPos('LV','image')
    uh = cv.getTrackbarPos('UH','image')
    us = cv.getTrackbarPos('US','image')
    uv = cv.getTrackbarPos('UV','image')
    
    l_b = np.array([lh,ls,lv])
    u_b = np.array([uh,us,uv])
    
    mask = cv.inRange(hsv, l_b, u_b) #thresholding the hsv image to get only blue colors
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    
    
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()