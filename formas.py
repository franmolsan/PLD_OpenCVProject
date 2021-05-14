import cv2
import numpy as np

x = 50
y = 50

camara = cv2.VideoCapture(0)

if camara.isOpened() is True:
    
    anchoframe = int(camara.get(cv2.CAP_PROP_FRAME_WIDTH))
    altoframe = int(camara.get(cv2.CAP_PROP_FRAME_HEIGHT))

    path = r'C:\Users\franm\Desktop\logo.png'

    logo = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    alto, ancho, canales = logo.shape
    
    b,g,r,a = cv2.split(logo) # dividir canales de la imagen: b,g,r y transparencia (alfa)
    logo = cv2.merge([b,g,r]) # componemos la imagen pero sin canal alfa, ya que lo usuaremos para hacer la máscara


    # a = 0 si ese pixel es transparente, si no, tiene valor
    a = a / 255.0
    alfa = cv2.merge([a,a,a])

    while camara.isOpened() is True:
        ret, frame = camara.read()
        if ret is True:
            frame[y:y+alto, x:x+ancho] = alfa * logo + (1-alfa) * frame[y:y+alto, x:x+ancho]

            cv2.imshow("MOSCA",frame)

        if cv2.waitKey(20)==ord(' '):
            break
    
    camara.release()
    cv2.destroyAllWindows()
