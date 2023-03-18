
import cv2

file = "frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(file)


webcam = cv2.VideoCapture(0)

count = 0

while True:

    (_,image) = webcam.read()
    auxImage = image.copy()

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=3)

    key = cv2.waitKey(10)
    ##print(f'Caras detectadas = {len(faces)}')

    for (x,y,w,h) in faces:
        
        cv2.rectangle(image, (x,y), (x+w, y+h), (128,0,255),2)

        rostro = auxImage[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)

        if key == ord('s'):
            #cv2.imwrite(f'Rostros_encontrados {count}',rostro)
            cv2.imshow('rostro',rostro)
            count =+ 1
        
    cv2.putText(image,'Detectando rostros',(10,20),2,0.5,(255,0,0),1,cv2.LINE_AA)
    cv2.putText(image,'Presione S para capturar rostro',(10,40),2,0.5,(255,0,0),1,cv2.LINE_AA)
    cv2.imshow('OpenCV',image)

    

    if key == 27:
        break










