import cv2

capture = cv2.VideoCapture("data/videos/wikipedia_donate.mp4")

while True:
    istrue, frame = capture.read()
    cv2.imshow('Video',frame)

    if cv2.waitKey(20) and 0xFF == ord('d'):
        break

    capture.release()
    cv2.destroyAllWindows()

# almost all cases in open cv the -215:Assertion failed means file couldn't be found.
# for video case the open cv ran out of the frames, and broke out of loop.