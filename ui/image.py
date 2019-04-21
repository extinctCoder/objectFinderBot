import time
import cv2
import imutils
from imutils.video import VideoStream
from img_aux import filter_colour, track_ball, draw_frame

cap = cv2.VideoCapture(0)


def module_img_ai():
    _, frame = cap.read()
    frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask = filter_colour(frame)
    location, _ = track_ball(mask)
    frame = draw_frame(mask, frame)
    return frame
