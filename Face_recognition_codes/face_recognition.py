import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')
people = ['cillian murphy', 'robert downey jr']
#features = np.load('features.npy', allow_pickle=True)
#labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'C:\Users\SOHAM MONDAL\PycharmProjects\opencv_1\faces\cillian murphy\images (3).jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in face_rect:
    faces_roi = gray[y:y+h, x:x+h]
    faces_roi = cv.resize(faces_roi, (100, 100))

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')
    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
cv.imshow('Detected Face', img)

cv.waitKey(0)
