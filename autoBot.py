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


if __name__ == "__main__":
    broadrcaster = get_broadrcaster()

    while True:
        forward_func()
    distroy_broadrcaster()
