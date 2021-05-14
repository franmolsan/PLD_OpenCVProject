import cv2
import numpy as np

img = np.zeros((250,250,3),np.uint8)

cv2.line(img, (50,50), (200,200), (0,255,0), 2)
cv2.rectangle(img, (70,130), (100,200), (255,0,0), -1) #num negativo en el grosor: se rellena
cv2.circle(img,(125,125), 70, (0,0,255), 1)

vertices = np.array([ [[20,30]], [[50,150]], [[200,15]], [[60,60]], [[150,50]] ])
cv2.polylines(img, [vertices], True, (0,255,255), 4)


cv2.imshow("dibujando", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
