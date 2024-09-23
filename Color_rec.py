import cv2 as cv

cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
while  True:
     _ , frame = cap.read()
     hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
     height, width, _ = frame.shape

     cx = int(width / 2)
     cy = int(height / 2)

     #Pick the pixel value 
     pixel_value = hsv_frame[cy, cx]
     hue_value = pixel_value[0]
     color ="undefined"

     if hue_value <  5:
         color = "red"
     elif hue_value < 22:
            color = "orange"
     elif hue_value <78 :
            color = "green" 
     elif hue_value < 131:
            color = "blue"                 
     pixel_center_bgr = frame[cy, cx]
     b , g , r  = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

     cv.rectangle(frame, (cx - 200,10), (cx+ 200 , 120), (255,255,255), -1)
     cv.putText(frame , color , (cx-200, 100), 0, 3, (b,g,r), 3)
     cv.circle(frame, (cx, cy), 5, (b,g,r), -1)
     cv.imshow("Frame", frame)
     key = cv.waitKey(1)
     if key == 27:
          break

cap.release()
cv.destroyAllWindows()    

 