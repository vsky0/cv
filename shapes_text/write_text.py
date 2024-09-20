import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def text_on_image(image, text):
    """
    writes the text on the image.
    """
    black_image = np.zeros((500,500,3) ,dtype='uint8')

    # write text on image
    cv.putText(img=image, text=text, org=(250,250), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=2, color=(0,0,0), thickness=4)
    cv.putText(img=black_image, text=text, org=(250,250), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=2, color=(255,255,255), thickness=4)
    
    fig, ax = plt.subplots(1,2, figsize=(10,5))

    ax[0].imshow(image)
    ax[0].set_title('TEXT ON IMAGE')
    ax[1].imshow(black_image)
    ax[1].set_title("TEXT ON BLACK IMAGE")
    plt.show()

if __name__ == '__main__':
    image = cv.imread('data/photos/cell.jpg')
    text = 'vsky'
    # calling the write text function
    text_on_image(image=image, text=text)
