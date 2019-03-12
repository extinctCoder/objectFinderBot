import math
from tkinter import *
import paho.mqtt.client as mqtt

broarcaster = None
red_max = 0
green_max = 0
blue_max = 0
red_min = 0
green_min = 0
blue_min = 0

hue_max_chanel = "objectFinderBot/colour/hue_max_chanel"
saturation_max_chanel = "objectFinderBot/colour/saturation_max_chanel"
value_max_chanel = "objectFinderBot/colour/value_max_chanel"
hue_min_chanel = "objectFinderBot/colour/hue_min_chanel"
saturation_min_chanel = "objectFinderBot/colour/saturation_min_chanel"
value_min_chanel = "objectFinderBot/colour/value_min_chanel"


def on_publish(client,userdata,result):
    print("Client: ", client)
    print("Userdata: : ", userdata)
    print("Result: ", result)
    return

def on_log(client, userdata, level, buf):
    print("Log: ",buf)
    return

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Mqtt client connected with broker")
        print("Preparing to send data")
    else:
        print("Unable to connect with broker. Error code: ", rc)
    return

def get_broarcaster():
    global broarcaster
    print("starting the mqtt calibration vroadcust module")
    broarcaster = mqtt.Client()
    broarcaster.on_connect = on_connect
    broarcaster.on_publish = on_publish
    broarcaster.on_log = on_log
    print("connecting with the server")
    broarcaster.connect("127.0.0.1")
    return broarcaster

def distroy_broarcaster():
    global broarcaster
    broarcaster.loop_stop()
    broarcaster.disconnect()
    return

def get_ui(title):
    mainGui = Tk()

    mainGui.geometry("460x300")
    mainGui.title(title)

    Label(mainGui, text="Maximium Clolor Space").grid(row=0, column=0)

    Label(mainGui, text="red_max").grid(row=1, column=0)
    Label(mainGui, text="First_max").grid(row=2, column=0)
    Label(mainGui, text="First_max").grid(row=3, column=0)

    Scale( mainGui, from_=0, to=255, command=update_r_max, orient=HORIZONTAL, length=340, width=20 ).grid(row=1, column=1)
    Scale( mainGui, from_=0, to=255, command=update_g_max, orient=HORIZONTAL, length=340, width=20 ).grid(row=2, column=1)
    Scale( mainGui, from_=0, to=255, command=update_b_max, orient=HORIZONTAL, length=340, width=20 ).grid(row=3, column=1)

    Label(mainGui, text="Minimum Clolor Space").grid(row=4, column=0)

    Label(mainGui, text="red_max").grid(row=5, column=0)
    Label(mainGui, text="First_max").grid(row=6, column=0)
    Label(mainGui, text="First_max").grid(row=7, column=0)

    Scale( mainGui, from_=0, to=255, command=update_r_min, orient=HORIZONTAL, length=340, width=20 ).grid(row=5, column=1)
    Scale( mainGui, from_=0, to=255, command=update_g_min, orient=HORIZONTAL, length=340, width=20 ).grid(row=6, column=1)
    Scale( mainGui, from_=0, to=255, command=update_b_min, orient=HORIZONTAL, length=340, width=20 ).grid(row=7, column=1)

    return mainGui



def update_r_max(val):
    global red_max
    red_max = val
    update_rgb(True, "RGB_MAX: ", red_max, green_max, blue_max)
    return 
def update_g_max(val):
    global green_max
    green_max = val
    update_rgb(True, "RGB_MAX: ", red_max, green_max, blue_max)
    return
def update_b_max(val):
    global blue_max
    blue_max = val
    update_rgb(True, "RGB_MAX: ", red_max, green_max, blue_max)
    return

def update_r_min(val):
    global red_min
    red_min = val
    update_rgb(False, "RGB_MIN: ", red_min, green_min, blue_min)
    return 
def update_g_min(val):
    global green_min
    green_min = val
    update_rgb(False, "RGB_MIN: ", red_min, green_min, blue_min)
    return
def update_b_min(val):
    global blue_min
    blue_min = val
    update_rgb(False, "RGB_MIN: ", red_min, green_min, blue_min)
    return

def update_rgb(isMax, txt, red, green, blue):
    global broarcaster
    print(txt, red, green, blue)
    h, s, v = rgb2hsv(red, green, blue)
    print ("HSV VALUE : ", h, s, v)
    if isMax:
        broarcaster.publish(hue_max_chanel, h)
        broarcaster.publish(saturation_max_chanel, s)
        broarcaster.publish(value_max_chanel, v)
        return
    else:
        broarcaster.publish(hue_min_chanel, h)
        broarcaster.publish(saturation_min_chanel, s)
        broarcaster.publish(value_min_chanel, v)
    return
    
def rgb2hsv(red, green, blue):
    red = float(red)
    green = float(green)
    blue = float(blue)
    red, green, blue = red/255.0, green/255.0, blue/255.0
    maximum = max(red, green, blue)
    minimum = min(red, green, blue)
    df = maximum-minimum
    if maximum == minimum:
        hue = 0
    elif maximum == red:
        hue = (60 * ((green-blue)/df) + 360) % 360
    elif maximum == green:
        hue = (60 * ((blue-red)/df) + 120) % 360
    elif maximum == blue:
        hue = (60 * ((red-green)/df) + 240) % 360
    if maximum == 0:
        saturation = 0
    else:
        saturation = df/maximum
    value = maximum
    return (hue, saturation, value)
