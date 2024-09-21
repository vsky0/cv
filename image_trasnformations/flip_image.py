import cv2 as cv

def flip(image, axis:int):
    """
    Flips an image along the specified axis.

    Args:
        image: input image to perform the flip.
        axis: 0 for horizontal, 1 for vertical, -1 for both vertical and horizontal.
    Return:
        flipped image.
    """
    return cv.flip(image, axis)

if __name__ == '__main__':
    print("SELECT 0 FOR HORIZONTAL FLIP ( ALONG X-AXIS)")
    print("SELECT 1 FOR VERTICAL FLIP ( ALONG Y-AXIS)")
    print("SELECT -1 FOR HORIZONTAL AND VERTICAL FLIP ( ALONG X,Y-AXIS)")

    axis = int(input("Enter an axis to flip along:"))
    
    if axis not in [-1, 0, 1]:
        print("Invalid choice.")
        exit()
    
    img = cv.imread('computer_vision/data/photos/simpsons1.jpg')
    cv.imshow('original image', img)

    img1 = flip(image=img, axis=axis)
    cv.imshow('fipped image', img1)

    cv.waitKey(0)
