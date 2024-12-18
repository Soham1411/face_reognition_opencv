import cv2 as cv
img = cv.imread('photos/cat.jpg')
cv.imshow('Cat',img)

# converting an image to grey scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# how to blurr an image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# dilating is the image
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilated)

# eroding
eroded = cv.erode(dilated,(7,7),iterations=1)
cv.imshow('Erode',eroded)

# resize
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# cropping
cropped = img[50:200, 200:400]
cv.imshow('Crops',cropped)

cv.waitKey(0)