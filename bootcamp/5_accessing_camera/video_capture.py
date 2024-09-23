import cv2 as cv
import sys

s = 0 # for the default camera

# check if any input source is provided while executing the program
if len(sys.argv)>1:
    s = sys.argv[1]

source = cv.VideoCapture(s)

window_name = 'camera'
cv.namedWindow(window_name, cv.WINDOW_NORMAL)

while cv.waitKey(1) != 27: #escape
    has_frame,frame = source.read()
    if not has_frame:
        break
    cv.imshow(window_name,frame)

source.release()
cv.destroyAllWindows()
# cv.destroyWindow(window_name)