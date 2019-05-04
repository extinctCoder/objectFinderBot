import time
import cv2
import imutils
from imutils.video import VideoStream
from img_aux import filter_colour, track_ball, draw_frame
import paho.mqtt.client as mqtt

MQTT_BROKER = "192.168.0.117"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 6000

command_motor_direction = "objectFinderBot/motor/command/direction"
command_motor_speed = "objectFinderBot/motor/command/speed"


def get_broadrcaster():
    global broadrcaster
    broadrcaster = mqtt.Client()
    print("connecting with the server")
    broadrcaster.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
    print("Server connected")
    return broadrcaster


def module_img_ai(title, camera, ifImg):
    videoStream = cv2.VideoCapture('http://192.168.0.117:8081')
    print("PLEASE WAIT WHILE MODULE INITIALIZE THE CAMERA MODILE")
    time.sleep(2.0)
    global broadrcaster, command_motor_direction, command_motor_speed
    broadrcaster = get_broadrcaster()
    while True:
        _, frame = videoStream.read()
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        mask = filter_colour(frame)
        location, _ = track_ball(mask)
        frame = draw_frame(mask, frame)
        x, y, w, h = location
        if(x >= 1):
            if(x <= 200):
                print("left movement x")
                broadrcaster.publish(command_motor_direction, 1)
        if(x >= 401):
            if(x <= 600):
                print("right movement x")
                broadrcaster.publish(command_motor_direction, 3)
        if(x >= 201):
            if(x <= 400):
                print("forworad movment")
                broadrcaster.publish(command_motor_direction, 0)
        if(x == 0):
            print("object not found")
            broadrcaster.publish(command_motor_direction, 4)
        if ifImg:
            cv2.imshow(title, frame)
            # cv2.imshow("maskFrame", hsv)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
    videoStream.stop()
    cv2.destroyAllWindows()
    return


module_img_ai("module_img_ai", 0, True)
