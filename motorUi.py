import time
from tkinter import *
import paho.mqtt.client as mqtt

# Define Variables
MQTT_BROKER = "192.168.0.117"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 6000

hand_speed_factor = 0.00
broadrcaster = None

max_inc = 255.00
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
    return


def left_func():
    global broadrcaster, command_motor_direction
    broadrcaster.publish(command_motor_direction, 1)
    return


def backward_func():
    global broadrcaster, command_motor_direction
    broadrcaster.publish(command_motor_direction, 2)
    return


def right_func():
    global broadrcaster, command_motor_direction
    broadrcaster.publish(command_motor_direction, 3)
    return


def stop_func():
    global broadrcaster, command_motor_direction
    broadrcaster.publish(command_motor_direction, 4)
    return


def speed_func(val):
    global broadrcaster, command_motor_speed
    broadrcaster.publish(command_motor_speed, val)
    return


def forward(args):
    forward_func()
    return


def left(args):
    left_func()
    return


def backward(args):
    backward_func()
    return


def right(args):
    right_func()
    return


def stop(args):
    stop_func()
    return


mainGui = Tk()
broadrcaster = get_broadrcaster()

mainGui.title("extinctCoder")

forward_btn = (Button(mainGui, text="forward",
                      command=forward_func, height=2, width=20, bg="green"))
left_btn = Button(mainGui, text="left",
                  command=left_func, height=2, width=20, bg="blue")
backward_btn = Button(mainGui, text="backward",
                      command=backward_func, height=2, width=20, bg="blue")
right_btn = Button(mainGui, text="right",
                   command=right_func, height=2, width=20, bg="blue")
speed_scale = Scale(mainGui, from_=min_dec, to=max_inc,
                    command=speed_func, orient=HORIZONTAL, width=20)

forward_btn.grid(row=0, column=1)
left_btn.grid(row=1, column=0)
backward_btn.grid(row=1, column=1)
right_btn.grid(row=1, column=2)
speed_scale.grid(row=2, column=0, columnspan=6, sticky='EW')


mainGui.bind("<KeyPress-w>", forward)
mainGui.bind("<KeyRelease-w>", stop)
mainGui.bind("<KeyPress-a>", left)
mainGui.bind("<KeyRelease-a>", stop)
mainGui.bind("<KeyPress-s>", backward)
mainGui.bind("<KeyRelease-s>", stop)
mainGui.bind("<KeyPress-d>", right)
mainGui.bind("<KeyRelease-d>", stop)

mainGui.mainloop()
distroy_broadrcaster()
