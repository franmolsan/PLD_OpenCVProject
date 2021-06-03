import cv2

# datos de reconocimiento facial, en el fichero xml
# que se ha generado en un aprendizaje previo
caraxml = "C:\Python39\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml"
sonrisaxml = "C:\Python39\Lib\site-packages\cv2\data\haarcascade_smile.xml"

# funciona con imagenes grises, en un solo canal
cc_cara = cv2.CascadeClassifier(caraxml)
cc_sornisa = cv2.CascadeClassifier(sonrisaxml)

camara = cv2.VideoCapture(0)

while camara.isOpened() is True:
    ret,frame = camara.read()
    if ret is True:
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        caras = cc_cara.detectMultiScale(gris, scaleFactor=1.2, minNeighbors=3, minSize=(90,90))
        for (cx,cy,cw,ch) in caras:
            cv2.rectangle(frame, (cx,cy), (cx+cw, cy+ch),(0,255,0),2)
            sonrisas = cc_sornisa.detectMultiScale(gris[cy:cy+ch,cx:cx+cw], scaleFactor=1.4, minNeighbors=7, minSize=(30,30))

            for (sx,sy,sw,sh) in sonrisas:
                cv2.rectangle(frame, (cx+sx,cy+sy), (cx+sx+sw, cy+sy+sh),(255,255,0),2)

        cv2.imshow("CARAS", frame)
        if cv2.waitKey(20) == ord(' '):
            break

cv2.destroyAllWindows()
