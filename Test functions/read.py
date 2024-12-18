import cv2 as cv
#reading images
# img = cv.imread('photos/cat2.jpg')
# cv.imshow('Cat', img)
# reading vedios
capture = cv.VideoCapture('vedios/vedio2.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Vedio',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

