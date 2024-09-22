import cv2 as cv
import numpy as np

img = cv.imread('computer_vision/data/photos/simpsons1.jpg')
cv.imshow('orignal image', img)

#splitting
b,g,r = cv.split(img)

cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

print(f"{img.shape}")
print(f"blue channel: {b.shape}")
print(f'green channel: {g.shape}')
print(f'red  channel: {r.shape}')

# merging
merged_image = cv.merge([b,g,r])
cv.imshow('merged image', merged_image)

# show original color channels.
black = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b, black, black])
green = cv.merge([black, g, black])
red = cv.merge([black, black, r])

cv.imshow('blue channel in image', blue)
cv.imshow('green channel in image', green)
cv.imshow('red channel in image', red)


cv.waitKey(0)