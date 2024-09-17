import numpy as np
import cv2

image = np.zeros((512,512,3), np.uint8)

img = cv2.line(image, (0,0), (511,511), (255,127,0), 5)
img = cv2.rectangle(image, (384,0), (510,128), (0,255,0), 3)
img = cv2.circle(image, (447,63), 63, (0,0,255), -1)
img = cv2.ellipse(image, (256,256), (100,50), 0, 0, 180, (255,0,0), -1)
img = cv2.arrowedLine(image, (0,0), (255,255), (255,0,0), 5)
font= cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(image, 'OpenCV', (10,100), font, 4, (255,255,255), 10, cv2.LINE_AA)
pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
img = cv2.polylines(image, [pts], True, (0,255,255), 3)




cv2.imshow('Black Rectangle (Color)', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print(image.shape)