import cv2 as cv

import numpy as np

img = cv.imread('data/photos/mitochondria.jpg')
# cv.imshow('Mitochondria', img)

# we can draw the original image and also use blank image.

# blank image

blank_image = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank Image', blank_image)


# paint the image green color
blank_image[:] = 0,255,0
cv.imshow('Green Image', blank_image)

#paint the image red color
blank_image[:] = 0,0,255
cv.imshow('RED IMAGE', blank_image)

# paint image blue color
blank_image[:] = 255,0,0
cv.imshow('BLUE IMAGE', blank_image)


# draw rectangle
cv.rectangle(blank_image, (0,0), (250, 500), (0,0,0), thickness=2)
# to fill the rectangle use -1.
cv.imshow('Rectangle', blank_image)

# draw circle
cv.circle(blank_image, (250,250), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank_image)

# draw line
cv.line(blank_image, (0,0), (500, 500), (255,255,255), thickness=5)
cv.imshow('lINE', blank_image)
cv.waitKey(0)