import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')
capture = cv.VideoCapture(0)

if not capture.isOpened():
    print("Error: Could not access the webcam.")
    exit()

while True:
    ret, frame = capture.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)
    print(f'Number of faces detected = {len(faces_rect)}')

    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    cv.imshow('Real-Time Face Detection', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
