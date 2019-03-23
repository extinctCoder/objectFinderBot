from __future__ import division
import paho.mqtt.client as mqtt
import Adafruit_PCA9685
import logging
import time

logging.basicConfig(level=logging.DEBUG)

topic =  "objectFinderBot/hand/command/#"

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

servo_min = 200
servo_max = 600

first_degree_min = 200
first_degree_max = 600

second_degree_min = 200
second_degree_max = 600

third_degree_min = 200
third_degree_max = 600

fourth_degree_min = 200
fourth_degree_max = 600

fifth_degree_min = 200
fifth_degree_max = 600

claw_min = 200
claw_max = 600

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
    global command_first_degree, command_second_degree, command_third_degree, command_fourth_degree, command_fifth_degree, command_claw
    if(message.topic == command_first_degree):
        angle_value = map_value(int(str(message.payload.decode("utf-8"))), fifth_degree_max, first_degree_min)
        print("command_first_degree_update : {}".format(angle_value))
    elif(message.topic == command_second_degree):
        angle_value = map_value(int(str(message.payload.decode("utf-8"))), fifth_degree_max, first_degree_min)
        print("command_second_degree : {}".format(angle_value))
        pass
    elif(message.topic == command_third_degree):
        angle_value = map_value(int(str(message.payload.decode("utf-8"))), fifth_degree_max, first_degree_min)
        print("command_third_degree : {}".format(angle_value))
        pass
    elif(message.topic == command_fourth_degree):
        angle_value = map_value(int(str(message.payload.decode("utf-8"))), fifth_degree_max, first_degree_min)
        print("command_fourth_degree : {}".format(angle_value))
        pass
    elif(message.topic == command_fifth_degree):
        angle_value = map_value(int(str(message.payload.decode("utf-8"))), fifth_degree_max, first_degree_min)
        print("command_fifth_degree : {}".format(angle_value))
        pass
    elif(message.topic == command_claw):
        angle_value = map_value(int(str(message.payload.decode("utf-8"))), fifth_degree_max, first_degree_min)
        print("command_claw : {}".format(angle_value))
        pass


    # print ("Message received: ", str(message.payload))
    # print ("Message topic: ", message.topic)
    # print ("Message qos: ", message.qos)
    # print ("Message retain flag: ", message.retain)
    return

def on_log(client, userdata, level, buf):
    print("Log: ", buf)
    return


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print ("Mqtt client connected with broker")
        client.subscribe(topic)
    else:
        print ("Unable to connect with broker. Error code:", rc)

print("Wellcome to mqtt broker subscribe script")
print("Creating new instance of mqtt client")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# client.on_log = on_log
print("Connecting to mqtt broker")
client.connect("127.0.0.1")
client.loop_forever()
