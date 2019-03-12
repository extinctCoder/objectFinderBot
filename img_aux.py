import cv2
import imutils
import numpy as np
from collections import deque

pts = deque(maxlen=64)

def filter_colour(frame):
    bgr_hsv =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    filter_one = cv2.inRange(bgr_hsv, np.array([160, 160,10]), np.array([190,255,255]))
    bgr_crcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    filter_two =cv2.inRange(bgr_crcb, np.array((0.,165.,0.)), np.array((255.,255.,255.)))
    c_filter = filter_one | filter_two
    c_filter = cv2.erode(c_filter, np.ones((8,8),np.uint8))
    c_filter = cv2.dilate(c_filter, np.ones((3,3),np.uint8))
    return c_filter
    
def track_ball(filter):
    area = 0
    index = 0
    position = (0,0,0,0)
    temp_contours, _ = cv2.findContours(filter, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    for temp_index, temp_contour in enumerate(temp_contours):
        temp_area = cv2.contourArea(temp_contour)
        if temp_area > area:
            area = temp_area
            index = temp_index
    if len(temp_contours) > 0:
        position = cv2.boundingRect(temp_contours[index])
    return (position, area)

def draw_frame(filter, frame):
    cnts = imutils.grab_contours(cv2.findContours(filter.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE))
    center = None
    if len(cnts) > 0:
        ((x, y), radius) = cv2.minEnclosingCircle(max(cnts, key=cv2.contourArea))
        M = cv2.moments(max(cnts, key=cv2.contourArea))
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
    pts.appendleft(center)
    for i in range(1, len(pts)):
        if pts[i - 1] is None or pts[i] is None:
            continue
        cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), int(np.sqrt(64 / float(i + 1)) * 2.5))
    return frame
