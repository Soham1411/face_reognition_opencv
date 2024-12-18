import cv2 as cv
import numpy as np

img = cv.imread('photos/cat.jpg')
cv.imshow('Cat',img)

# Translation, used to shift image along x and y
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
# -x --> left
# -y --> up
# x --> right
# y --> down
translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# Rotation, used to rotate the image
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)
    return cv.warpAffine(img, rotMat, dimensions)
rotated = rotate(img,45)
cv.imshow('Rotated', rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resize', resized)

# Flipping
flip = cv.flip(img,1)
# 1 - flip the image as mirror image,
# 0 - flips the image by 180 degree,
# -1 is flip by both x axis and y axis
cv.imshow('Flip',flip)

# cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)