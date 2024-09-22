import cv2 as cv

# contours are the borders/boundaries of the objects
# in the image, contour detection is used in object detection,
# image recognition

img = cv.imread('computer_vision/data/photos/bonsai_tree.jpg')

# first convert the image into gray

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray image', gray_img)

# blur the image, then pass it to the canny input
blur_img = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur image', blur_img)

# find the edges, of the image, doing using canny

img_edges = cv.Canny(img, 125, 175) # here the 125, 175 are the threshold values.
cv.imshow('edges in the image', img_edges)

# contours with thresholding
ret, thresh = cv.threshold(gray_img, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresholded', thresh)

# now apply findContours method to img_edges
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"the number of contours in image={len(contours)}")

cv.waitKey(0)

# applying blur to images reduces noise and provides only significant contors, while unblurred image 
# can have more contours.

# using the thresholding to find the no. of contours(171) is less by 3 of canny edge(174).