from tkinter import *
import paho.mqtt.client as mqtt
# Define Variables
MQTT_BROKER = "127.0.0.1"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45

hand_speed_factor = 0.00
broadrcaster = None

max_inc = 100.00
min_dec = 0.00

speed = 0.00
is_speed_first_degree = False
is_speed_second_degree = False
is_speed_third_degree = False
is_speed_fourth_degree = False
is_speed_fifth_degree = False
is_speed_claw = False

command_first_degree = "objectFinderBot/hand/command/first_degree"
command_second_degree = "objectFinderBot/hand/command/second_degree"
command_third_degree = "objectFinderBot/hand/command/third_degree"
command_fourth_degree = "objectFinderBot/hand/command/fourth_degree"
command_fifth_degree = "objectFinderBot/hand/command/fifth_degree"
command_claw = "objectFinderBot/hand/command/claw"

feedback_first_degree = "objectFinderBot/hand/feedback/first_degree"
feedback_second_degree = "objectFinderBot/hand/feedback/second_degree"
feedback_third_degree = "objectFinderBot/hand/feedback/third_degree"
feedback_fourth_degree = "objectFinderBot/hand/feedback/fourth_degree"
feedback_fifth_degree = "objectFinderBot/hand/feedback/fifth_degree"
feedback_claw = "objectFinderBot/hand/feedback/claw"

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
        print("Broadcaster client connected with the server")
    else:
        print("Unable to connect with server. Error code: ", rc)
    return

def get_broadrcaster():
    global broadrcaster
    print("starting the mqtt calibration vroadcust module")
    broadrcaster = mqtt.Client()
    broadrcaster.on_connect = on_connect
    broadrcaster.on_publish = on_publish
    broadrcaster.on_log = on_log
    print("connecting with the server")
    broadrcaster.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
    return broadrcaster

def distroy_broadrcaster():
    global broadrcaster
    broadrcaster.loop_stop()
    broadrcaster.disconnect()
    return


def first_degree_inc_update_func():
    global broadrcaster, speed, hand_speed_factor, max_inc
    if(speed + hand_speed_factor <= max_inc):
        speed += hand_speed_factor
        pass
    broadrcaster.publish(command_first_degree, speed)
    return
def first_degree_dec_update_func():
    global broadrcaster, speed, hand_speed_factor, min_dec
    if(speed - hand_speed_factor >= min_dec):
        speed -= hand_speed_factor
        pass
    broadrcaster.publish(command_first_degree, speed)
    return

def second_degree_inc_update_func():
    global broadrcaster, speed, hand_speed_factor, max_inc
    if(speed + hand_speed_factor <= max_inc):
        speed += hand_speed_factor
        pass
    broadrcaster.publish(command_second_degree, speed)
    return
def second_degree_dec_update_func():
    global broadrcaster, speed, hand_speed_factor, min_dec
    if(speed - hand_speed_factor >= min_dec):
        speed -= hand_speed_factor
        pass
    broadrcaster.publish(command_second_degree, speed)
    return

def third_degree_inc_update_func():
    global broadrcaster, speed, hand_speed_factor, max_inc
    if(speed + hand_speed_factor <= max_inc):
        speed += hand_speed_factor
        pass
    broadrcaster.publish(command_third_degree, speed)
    return
def third_degree_dec_update_func():
    global broadrcaster, speed, hand_speed_factor, min_dec
    if(speed - hand_speed_factor >= min_dec):
        speed -= hand_speed_factor
        pass
    broadrcaster.publish(command_third_degree, speed)
    return

def fourth_degree_inc_update_func():
    global broadrcaster, speed, hand_speed_factor, max_inc
    if(speed + hand_speed_factor <= max_inc):
        speed += hand_speed_factor
        pass
    broadrcaster.publish(command_fourth_degree, speed)
    return
def fourth_degree_dec_update_func():
    global broadrcaster, speed, hand_speed_factor, min_dec
    if(speed - hand_speed_factor >= min_dec):
        speed -= hand_speed_factor
        pass
    broadrcaster.publish(command_fourth_degree, speed)
    return

def fifth_degree_inc_update_func():
    global broadrcaster, speed, hand_speed_factor, max_inc
    if(speed + hand_speed_factor <= max_inc):
        speed += hand_speed_factor
        pass
    broadrcaster.publish(command_fifth_degree, speed)
    return
def fifth_degree_dec_update_func():
    global broadrcaster, speed, hand_speed_factor, min_dec
    if(speed - hand_speed_factor >= min_dec):
        speed -= hand_speed_factor
        pass
    broadrcaster.publish(command_first_degree, speed)
    return

def claw_inc_update_func():
    global broadrcaster, speed, hand_speed_factor, max_inc
    if(speed + hand_speed_factor <= max_inc):
        speed += hand_speed_factor
        pass
    broadrcaster.publish(command_claw, speed)
    return
def claw_dec_update_func():
    global broadrcaster, speed, hand_speed_factor, min_dec
    if(speed - hand_speed_factor >= min_dec):
        speed -= hand_speed_factor
        pass
    broadrcaster.publish(command_claw, speed)
    return

def speed_update_func(val):
    global hand_speed_factor
    hand_speed_factor = int(val)
    return

mainGui = Tk()
broadrcaster = get_broadrcaster()

mainGui.title("extinctCoder")


Button(mainGui, text="first_degree_inc", command = first_degree_inc_update_func, height = 2, width = 20, bg = "blue").grid(row=0, column=0)
Button(mainGui, text="first_degree_dec", command = first_degree_dec_update_func, height = 2, width = 20, bg = "green").grid(row=1, column=0)
Label(mainGui, text="first_degree").grid(row=2, column=0)
# first_degree_txt = Label(mainGui).grid(row=3, column=0)

Button(mainGui, text="second_degree_inc", command = second_degree_inc_update_func, height = 2, width = 20, bg = "blue").grid(row=0, column=1)
Button(mainGui, text="second_degree_dec", command = second_degree_dec_update_func, height = 2, width = 20, bg = "green").grid(row=1, column=1)
Label(mainGui, text="second_degree").grid(row=2, column=1)
# second_degree_txt = Label(mainGui).grid(row=3, column=1)

Button(mainGui, text="third_degree_inc", command = third_degree_inc_update_func, height = 2, width = 20, bg = "blue").grid(row=0, column=2)
Button(mainGui, text="third_degree_dec", command = third_degree_dec_update_func, height = 2, width = 20, bg = "green").grid(row=1, column=2)
Label(mainGui, text="third_degree").grid(row=2, column=2)
# third_degree_txt = Label(mainGui).grid(row=3, column=2)

Button(mainGui, text="fourth_degree_inc", command = fourth_degree_inc_update_func, height = 2, width = 20, bg = "blue").grid(row=0, column=3)
Button(mainGui, text="fourth_degree_dec", command = fourth_degree_dec_update_func, height = 2, width = 20, bg = "green").grid(row=1, column=3)
Label(mainGui, text="fourth_degree").grid(row=2, column=3)
# fourth_degree_txt = Label(mainGui).grid(row=3, column=3)

Button(mainGui, text="fifth_degree_inc", command = fifth_degree_inc_update_func, height = 2, width = 20, bg = "blue").grid(row=0, column=4)
Button(mainGui, text="fifth_degree_dec", command = fifth_degree_dec_update_func, height = 2, width = 20, bg = "green").grid(row=1, column=4)
Label(mainGui, text="fifth_degree").grid(row=2, column=4)
# fifth_degree_txt = Label(mainGui).grid(row=3, column=4)

Button(mainGui, text="claw_inc", command = claw_inc_update_func, height = 2, width = 20, bg = "blue").grid(row=0, column=5)
Button(mainGui, text="claw_dec", command = claw_dec_update_func, height = 2, width = 20, bg = "green").grid(row=1, column=5)
Label(mainGui, text="claw").grid(row=2, column=5)
# claw_txt = Label(mainGui).grid(row=3, column=5)

Scale(mainGui, from_=0, to=10, command = speed_update_func, orient=HORIZONTAL, width=20).grid(row=4, column=0, columnspan=6, sticky='EW')
Label(mainGui, text="speed").grid(row=5, column=0, columnspan=6, sticky='EW')

mainGui.mainloop()
distroy_broadrcaster()
















'''def update_rgb(isMax, txt, red, green, blue):
    global broadrcaster
    print(txt, red, green, blue)
    h, s, v = rgb2hsv(red, green, blue)
    print ("HSV VALUE : ", h, s, v)
    if isMax:
        #broadrcaster.publish(hue_max_chanel, h)
        #broadrcaster.publish(saturation_max_chanel, s)
        broadrcaster.publish(value_max_chanel, v)
        return
    else:
        broadrcaster.publish(hue_min_chanel, h)
        broadrcaster.publish(saturation_min_chanel, s)
        broadrcaster.publish(value_min_chanel, v)
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
'''
