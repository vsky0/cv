import cv2 as cv
import numpy as np


def rotate_image(image, angle, rot_point=None):
    """
    Rotate an image around center if rot_point is None. else rotate around the given point.

    Args:
        image: image to rotate.
        angle: angle in degrees to rotate. for clockwise rotation use -ve sign.
        rot_point: rotatation point of the image, which is a tuple of pixel values.
    Return:
        rotated image around the given angle and rotation  point.
    """
    height, width = image.shape[:2]
    
    if rot_point is None:
        rot_point = (width//2, height//2)
    
    rot_mat = cv.getRotationMatrix2D(rot_point, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(image, rot_mat, dimensions)

if __name__ == '__main__':
    img = cv.imread('computer_vision/data/photos/cell.jpg')
    cv.imshow('original cell', img)

    img1 = rotate_image(image=img, angle=90)
    cv.imshow('rotated cell image', img1)

    cv.waitKey(0)