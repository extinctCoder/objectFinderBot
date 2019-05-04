from __future__ import division
import paho.mqtt.client as mqtt
from adafruit_servokit import ServoKit
import time

topic = "objectFinderBot/hand/command/#"


kit = ServoKit(channels=16)


first_degree_min = 0
first_degree_max = 180

second_degree_min = 0
second_degree_max = 110

third_degree_min = 15
third_degree_max = 180

fourth_degree_min = 0
fourth_degree_max = 180

fifth_degree_min = 0
fifth_degree_max = 180

claw_min = 50
claw_max = 120

first_pin = 0
second_pin = 14
third_pin = 10
fourth_pin = 7
fifth_pin = 12
sixth_pin = 13

command_first_degree = "objectFinderBot/hand/command/first_degree"
command_second_degree = "objectFinderBot/hand/command/second_degree"
command_third_degree = "objectFinderBot/hand/command/third_degree"
command_fourth_degree = "objectFinderBot/hand/command/fourth_degree"
command_fifth_degree = "objectFinderBot/hand/command/fifth_degree"
command_claw = "objectFinderBot/hand/command/claw"


def map_value(value, destination_max, destination_min):
    span = destination_max - destination_min
    value_scaled = float(value - 0.00) / 100.00

    return int(destination_min + (value_scaled * span))


def on_message(client, userdata, message):
    global pwm, command_first_degree, command_second_degree, command_third_degree, command_fourth_degree, command_fifth_degree, command_claw
    if(message.topic == command_first_degree):
        angle_value = map_value(
            int(str(message.payload.decode("utf-8"))), first_degree_max, first_degree_min)
        print("command_first_degree_update : {}".format(angle_value))
        kit.servo[first_pin].angle = angle_value
    elif(message.topic == command_second_degree):
        angle_value = map_value(int(str(message.payload.decode(
            "utf-8"))), second_degree_max, second_degree_min)
        print("command_second_degree : {}".format(angle_value))
        kit.servo[second_pin].angle = angle_value
    elif(message.topic == command_third_degree):
        angle_value = map_value(
            int(str(message.payload.decode("utf-8"))), third_degree_max, third_degree_min)
        print("command_third_degree : {}".format(angle_value))
        kit.servo[third_pin].angle = angle_value
    elif(message.topic == command_fourth_degree):
        angle_value = map_value(int(str(message.payload.decode(
            "utf-8"))), fourth_degree_max, fourth_degree_min)
        print("command_fourth_degree : {}".format(angle_value))
        kit.servo[fourth_pin].angle = angle_value
    elif(message.topic == command_fifth_degree):
        angle_value = map_value(
            int(str(message.payload.decode("utf-8"))), fifth_degree_max, fifth_degree_min)
        print("command_fifth_degree : {}".format(angle_value))
        kit.servo[fifth_pin].angle = angle_value
    elif(message.topic == command_claw):
        angle_value = map_value(
            int(str(message.payload.decode("utf-8"))), claw_max, claw_min)
        print("command_claw : {}".format(angle_value))
        kit.servo[sixth_pin].angle = angle_value
    return


def on_log(client, userdata, level, buf):
    print("Log: ", buf)
    return


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Mqtt client connected with broker")
        client.subscribe(topic)
    else:
        print("Unable to connect with broker. Error code:", rc)


print("Wellcome to mqtt broker subscribe script")
print("Creating new instance of mqtt client")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# client.on_log = on_log
print("Connecting to mqtt broker")
client.connect("192.168.0.117")
client.loop_forever()
