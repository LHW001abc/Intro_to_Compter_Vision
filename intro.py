import cv2
import numpy as np

# Load an image using 'imread' specifying the path to image
input = cv2.imread('./Intro_to_Compter_Vision/images.jpg' ,1)
 
cv2.imshow('Hello World', input)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('output.jpg', input)
    cv2.destroyAllWindows()


# cv2.waitKey(0) will display the window infinitely until any keypress (it is suitable for image display).    