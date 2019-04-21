import time
from tkinter import *
import paho.mqtt.client as mqtt

# Define Variables
MQTT_BROKER = "127.0.0.1"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 6000

hand_speed_factor = 0.00
broadrcaster = None

max_inc = 100.00
min_dec = 0.00


command_motor_direction = "objectFinderBot/motor/command/direction"
command_motor_speed = "objectFinderBot/motor/command/speed"


def get_broadrcaster():
    global broadrcaster
    broadrcaster = mqtt.Client()
    print("connecting with the server")
    broadrcaster.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
    print("Server connected")
    return broadrcaster


def distroy_broadrcaster():
    global broadrcaster
    broadrcaster.loop_stop()
    broadrcaster.disconnect()
    return


def forward_func():
    global broadrcaster, command_motor_direction
    broadrcaster.publish(command_motor_direction, 0)
    time.sleep(0.2)
    broadrcaster.publish(command_motor_direction, 4)
    return


def left_func():
    global broadrcaster, command_motor_direction
    broadrcaster.publish(command_motor_direction, 1)
    time.sleep(0.2)
    broadrcaster.publish(command_motor_direction, 4)
    return


def backward_func():
    global broadrcaster, command_motor_direction
    broadrcaster.publish(command_motor_direction, 2)
    time.sleep(0.2)
    broadrcaster.publish(command_motor_direction, 4)
    return


def right_func():
    global broadrcaster, command_motor_direction
    broadrcaster.publish(command_motor_direction, 3)
    time.sleep(0.2)
    broadrcaster.publish(command_motor_direction, 4)
    return


def speed_func(val):
    global broadrcaster, command_motor_speed
    broadrcaster.publish(command_motor_speed, val)
    return


mainGui = Tk()
broadrcaster = get_broadrcaster()

mainGui.title("extinctCoder")

forward_btn = (Button(mainGui, text="first_degree_inc",
                      command=forward_func, height=2, width=20, bg="green"))
left_btn = Button(mainGui, text="second_degree_inc",
                  command=left_func, height=2, width=20, bg="blue")
backward_btn = Button(mainGui, text="second_degree_dec",
                      command=backward_func, height=2, width=20, bg="blue")
right_btn = Button(mainGui, text="third_degree_inc",
                   command=right_func, height=2, width=20, bg="blue")
speed_scale = Scale(mainGui, from_=0, to=100,
                    command=speed_func, orient=HORIZONTAL, width=20)

forward_btn.grid(row=0, column=1)
left_btn.grid(row=1, column=0)
backward_btn.grid(row=1, column=1)
right_btn.grid(row=1, column=2)
speed_scale.grid(row=2, column=0, columnspan=6, sticky='EW')
mainGui.mainloop()
distroy_broadrcaster()
