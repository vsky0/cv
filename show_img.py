import cv2

img = cv2.imread('data/photos/cell.jpg')

cv2.imshow('Cell', img)

cv2.waitKey(0)