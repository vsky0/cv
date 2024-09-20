import cv2 as cv

def rescaled(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# video

def rescale_video():
    """
    use for rescaling videos.
    """
    capture = cv.VideoCapture('data/videos/wikipedia_donate.mp4')

    while True:
        is_true, frame = capture.read()

        frame_resized = rescaled(frame)
        cv.imshow('Video rescaled', frame_resized)

        cv.imshow('Video', frame)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break

    capture.release()
    cv.destroyAllWindows()

# image

def rescale_image():
    image = cv.imread('data/photos/cell.jpg')
    rescaled_image = rescaled(image, scale=0.5)
    cv.imshow('Rescaled image', rescaled_image)
    cv.imshow('original image', image)
    cv.waitKey(0)

# change the resolution of the live video.
def change_resolution(width, height):
    """
    this only works on the live video.
    """
    capture = cv.VideoCapture(0)
    capture.set(3, width)
    capture.set(4, height)

    while True:
        is_true, frame = capture.read()
        cv.imshow('Changed Resolution', frame)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    
    capture.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    print("Choose an option:")
    print("1 for rescaling image.")
    print("2 for rescaling video.")
    print("3 for changing resolution for video.")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        print("YOU'VE SELECTED THE RESCALING IMAGE.")
        print("YOU WILL SEE BOTH ORIGINAL AND RESCALED IMAGES.")

        rescale_image()
    elif choice == 2:
        print("YOU'VE SELECTED THE RESCALING VIDEO.")
        print("YOU WILL SEE BOTH ORIGINAL AND RESCALED VIDEOS.")
        rescale_video()
    elif choice == 3:
        print("YOU WILL SEE CHANGED RESOLUTION OF LIVE VIDEO.")
        change_resolution(10, 10)
    else:
        print("INVALID CHOICE")
