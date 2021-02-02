import cv2 as cv

# Reading Picture
img = cv.imread('photos/dog.jpg')

cv.imshow('Dog', img)

# Reading Video

cv.waitKey(0)
