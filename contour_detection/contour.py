import cv2 as cv

# contours are the borders/boundaries of the objects
# in the image, contour detection is used in object detection,
# image recognition

img = cv.imread('computer_vision/data/photos/geometric_shapes.jpg')

# first convert the image into gray

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray image', gray_img)

# second find the edges, of the image, doing using canny

img_edges = cv.Canny(img, 125, 175) # here the 125, 175 are the threshold values.
cv.imshow('edges in the image', img_edges)

# now apply findContours method to img_edges

contours, hierarchies = cv.findContours(img_edges, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"the number of countours find={len(contours)}")

cv.waitKey(5000)