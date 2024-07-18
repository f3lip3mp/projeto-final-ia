
import cv2
from deepface import DeepFace


#modelo de detectação de face utiliado
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


video = cv2.VideoCapture(0) #1 para webcam externa #0 para webcam integrada

while video.isOpened():
    ret, frame = video.read()
    #conversor de frame para escala cinza 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #detector
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=5)

    for x,y,w,h in face:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
        try:
            #analisa emoções da face
            analyze = DeepFace.analyze(frame, actions=['emotion'])
            #imprime a emoção dominante
            print(analyze[0]['dominant_emotion'])
        except:
            print('Rosto não identificado')

    cv2.imshow('video',frame)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break


video.release()


imgpath = '' #coloque o caminho inteiro da imagem


try:
    image = cv2.imread(imgpath)
    if image is not None:
        analyze = DeepFace.analyze(image, actions=['emotion'])
        print(analyze[0]['dominant_emotion'])
    else:
        print("Erro no carregamento da imagem")
except Exception as e:
    print("An error occurred:", e)

