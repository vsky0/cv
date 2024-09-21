import cv2 as cv
import numpy as np

# translating image using function below
def translate_image(image, x:int, y:int):
    """
    Translates the given image along x pixels on x-axis and y pixels on y-axis.
    uses a kernel to apply translation.
    Args:
        image: image you want to translate.
        x: number of pixels to translate along x-axis.
        y: number of pixels to translate along y-axis.
    Returns:
        transalted image
    """
    trans_kernel = np.float32([1, 0, x], [0, 1, y])
    dimensions = (image.shape[1], image.shape[0]) #width, height
    return cv.wrapAffine(image, trans_kernel, dimensions)

if __name__ == '__main__':
    img = cv.imread('data/photos/simpson1.jpg')
    cv.imshow('SIMPSON original', img)

    timg = translate_image(image=img, x=50, y=50)
    cv.imshow('SIMPSON TRANSLATED', timg)

    cv.waitKey(0)
    
