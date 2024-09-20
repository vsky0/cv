import cv2

img = cv2.imread('data/photos/cell.jpg')

cv2.imshow('Cell', img)

cv2.waitKey(0)

# for images whose size is greater thab the size of the window size,
# image is shown big covering more than size of window.