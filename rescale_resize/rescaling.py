import cv2 as cv

def rescaled(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# reading video

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
