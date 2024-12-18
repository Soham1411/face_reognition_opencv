import cv2 as cv
import numpy as np
blank = np.zeros((400,400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# Bitwise AND --> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise AND", bitwise_and)

# Bitwise OR -->  intersecting and non-intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise_OR', bitwise_or)

# Bitwise XOR --> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise_XOR', bitwise_xor)\

# Bitwise NOT
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise_Not', bitwise_not)

cv.waitKey(0)