
import cv2
from deepface import DeepFace


#modelo de detectação de face utiliado
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


video = cv2.VideoCapture(0) #1 para webcam externa #0 para webcam integrada

while video.isOpened():
    ret, frame = video.read()
    #conversor de frame para escala cinza 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('video',frame)
    
video.release()
