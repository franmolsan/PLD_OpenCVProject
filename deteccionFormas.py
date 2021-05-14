from types import ClassMethodDescriptorType
import cv2
import numpy as np

path = r'C:\Users\franm\Desktop\billar.jpg'

# img = cv2.imread(path)

camara = cv2.VideoCapture(0)

while camara.isOpened() is True:
    ret, frame = camara.read()

    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gris = cv2.GaussianBlur(gris, (7,7), 1)

    circulos = cv2.HoughCircles(gris, cv2.HOUGH_GRADIENT, 1.1, 100)
    if circulos is not None:
        circulos = np.round(circulos[0, :]).astype("int")

        for(x,y,r) in circulos:
            cv2.circle(frame, (x,y), r, (0,255,0), 5)

    cv2.imshow("dibujando", frame)

    
    if cv2.waitKey(20)==ord(' '):
        break


# gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gris = cv2.GaussianBlur(gris, (7,7), 1)

# circulos = cv2.HoughCircles(gris, cv2.HOUGH_GRADIENT, 1.5, 100)
# if circulos is not None:
#   circulos = np.round(circulos[0, :]).astype("int")


#    for(x,y,r) in circulos:
#        cv2.circle(img, (x,y), r, (0,255,0), 5)

# cv2.imshow("dibujando", img)

camara.release()
cv2.destroyAllWindows()
