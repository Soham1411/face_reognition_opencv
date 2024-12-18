import cv2 as cv
img = cv.imread('photos/cat2.jpg')
cv.imshow('Cat', img)
def rescaleFrame(frame, scale=0.75):
    #works with already existing vedios or images and also live vedios
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)
#def changeRes(width, height):
    #Works only for video
    #capture.set(3, width)
    #capture.set(4, height)

#reading vedios
capture = cv.VideoCapture('vedios/vedio2.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Vedio',frame)
    cv.imshow('Vedio Resized', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()