import cv2
import numpy as np


path = r'C:\Users\franm\Desktop\sudoku.jpg'

sudoku = cv2.imread(path)

gris = cv2.cvtColor(sudoku, cv2.COLOR_BGR2GRAY)

# suavizado para eliminar el ruido
gris = cv2.GaussianBlur(gris, (11,11), 0)

# umbralización adaptativa, no es común para toda la imagen, se calcula en cada "vecindad"
bin = cv2.adaptiveThreshold(gris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# bin2 = cv2.adaptiveThreshold(gris, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)


ret, otsu = cv2.threshold(gris, 127 , 255 ,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("OTSU", otsu)
cv2.imshow("GAUSSIANA", bin)


cv2.waitKey(0)
cv2.destroyAllWindows()
