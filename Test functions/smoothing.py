import cv2 as cv

img = cv.imread('photos/cat.jpg')
cv.imshow("Cats", img)

# Averaging
average = cv.blur(img,(3,3))
cv.imshow('Average Blur', average)

# Gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral Blur", bilateral)

cv.waitKey(0)