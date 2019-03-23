import time
import cv2
import imutils
from imutils.video import VideoStream
from img_aux import filter_colour, track_ball, draw_frame

def module_img_ai(title, camera, ifImg):
    videoStream = VideoStream(src = camera).start()
    print("PLEASE WAIT WHILE MODULE INITIALIZE THE CAMERA MODILE")
    time.sleep(2.0) 
    while True:
        frame = imutils.resize(videoStream.read(), width=600)
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        
        mask = filter_colour(frame)
        location , _ = track_ball(mask)
        frame = draw_frame(mask, frame)
        x,y,w,h = location
        if(x >= 1):
            if(x <= 200 ):
                print ("right movement")
        if(x >= 401):
            if(x <= 600):
                print("left movement")
        if(x >= 201):
            if(x <= 400):
                print("forworad movment")
        if(x == 0):
            print("object not found")
        if ifImg:
            cv2.imshow(title, frame)
            cv2.imshow("maskFrame", hsv)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
    videoStream.stop()
    cv2.destroyAllWindows()
    return

module_img_ai("abc", 4, True)
