import cv2 as cv


def resize_img(image, size:tuple):
    """
    Resize the image to the specific size. if you shrink image use the `interpolation=cv.INTER_LINEAR`, if you enlarge image us the `interpolation=cv.INTER_AREA`/`cv.INTER_CUBIC` for good resolution.

    Args:
        image: input image to resize.
        size: tuple of pixel values to resize.
    Return:
        resized image to the given input size.
    """
    return cv.resize(image, size, interpolation=cv.INTER_CUBIC)
    

if __name__ == '__main__':
    img = cv.imread('computer_vision/data/photos/cell100.jpg')
    cv.imshow('original image', img)

    img1 = resize_img(image=img, size=(750,750))
    cv.imshow('resized image', img1)

    cv.waitKey(0)