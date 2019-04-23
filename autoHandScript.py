import time
from tkinter import *
import paho.mqtt.client as mqtt
# Define Variables
MQTT_BROKER = "192.168.0.117"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 6000

speed_factor = .75
broadrcaster = None


first_degree_old = 61
second_degree_old = 5
third_degree_old = 4
fourth_degree_old = 53
fifth_degree_old = 11
claw_old = 79

first_degree = 0
second_degree = 0
third_degree = 0
fourth_degree = 0
fifth_degree = 0
claw = 0

command_first_degree = "objectFinderBot/hand/command/first_degree"
command_second_degree = "objectFinderBot/hand/command/second_degree"
command_third_degree = "objectFinderBot/hand/command/third_degree"
command_fourth_degree = "objectFinderBot/hand/command/fourth_degree"
command_fifth_degree = "objectFinderBot/hand/command/fifth_degree"
command_claw = "objectFinderBot/hand/command/claw"


def on_log(client, userdata, level, buf):
    print("Log: ", buf)
    return


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Mqtt client connected with broker")
        client.subscribe(topic)
    else:
        print("Unable to connect with broker. Error code:", rc)


def get_broadrcaster():
    global broadrcaster
    print("starting the mqtt calibration vroadcust module")
    broadrcaster = mqtt.Client()
    broadrcaster.on_connect = on_connect
    broadrcaster.on_log = on_log
    print("connecting with the server")
    broadrcaster.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
    return broadrcaster


def update_position():
    global speed_factor
    global first_degree, second_degree, third_degree, fourth_degree, fifth_degree, claw
    global first_degree_old, second_degree_old, third_degree_old, fourth_degree_old, fifth_degree_old, claw_old
    global broadrcaster, command_first_degree, command_second_degree, command_third_degree, command_fourth_degree, command_fifth_degree, command_claw

    print('fist_degree: {0}  fist_degree_old : {1}'.format(
        str(first_degree), str(first_degree_old)))
    print('srcond_degree: {0}  second_degree_old : {1}'.format(
        str(second_degree), str(second_degree_old)))
    print('third_degree: {0}  third_degree_old : {1}'.format(
        str(third_degree), str(third_degree_old)))
    print('fourth_degree: {0}  fourth_degree_old : {1}'.format(
        str(fourth_degree), str(fourth_degree_old)))
    print('fifth_degree: {0}  fist_degree_old : {1}'.format(
        str(fifth_degree), str(fifth_degree_old)))
    print('claw: {0}  claw_old : {1}'.format(
        str(claw), str(claw_old)))

    if(first_degree == first_degree_old):
        print('sending command in chanel : {0} the command is : {1}'.format(
            str(command_first_degree), str(first_degree)))
        broadrcaster.publish(command_first_degree, int(first_degree))
        time.sleep(speed_factor)
        print("--command send")
    else:
        if(first_degree < first_degree_old):
            for movement in range(first_degree, first_degree_old, 1):
                print('sending command in chanel : {0} the command is : {1}'.format(
                    str(command_first_degree), str(movement)))
                broadrcaster.publish(command_first_degree, int(movement))
                time.sleep(speed_factor)
                print("--command send")
        elif(first_degree > first_degree_old):
            for movement in range(first_degree_old, first_degree, 1):
                print('sending command in chanel : {0} the command is : {1}'.format(
                    str(command_first_degree), str(movement)))
                broadrcaster.publish(command_first_degree, int(movement))
                time.sleep(speed_factor)
                print("--command send")

    if(second_degree == second_degree_old):
        print('sending command in chanel : {0} the command is : {1}'.format(
            str(command_second_degree), str(second_degree)))
        broadrcaster.publish(command_second_degree, int(second_degree))
        time.sleep(speed_factor)
        print("--command send")
    else:
        if(second_degree < second_degree_old):

            for movement in range(second_degree, second_degree_old, 1):
                print('sending command in chanel : {0} the command is : {1}'.format(
                    str(command_second_degree), str(movement)))
                broadrcaster.publish(command_second_degree, int(movement))
                time.sleep(speed_factor)
                print("--command send")
        elif(second_degree < second_degree_old):
            for movement in range(second_degree_old, second_degree, 1):
                print('sending command in chanel : {0} the command is : {1}'.format(
                    str(command_second_degree), str(movement)))
                broadrcaster.publish(command_second_degree, int(movement))
                time.sleep(speed_factor)
                print("--command send")

    if(third_degree == third_degree_old):
        print('sending command in chanel : {0} the command is : {1}'.format(
            str(command_third_degree), str(third_degree)))
        broadrcaster.publish(command_third_degree, int(third_degree))
        time.sleep(speed_factor)
        print("--command send")
    else:
        if(third_degree < third_degree_old):
            for movement in range(third_degree, third_degree_old, 1):
                print('sending command in chanel : {0} the command is : {1}'.format(
                    str(command_third_degree), str(movement)))
                broadrcaster.publish(command_third_degree, int(movement))
                time.sleep(speed_factor)
                print("--command send")
        elif(third_degree < third_degree_old):
            for movement in range(third_degree_old, third_degree, 1):
                print('sending command in chanel : {0} the command is : {1}'.format(
                    str(command_third_degree), str(movement)))
                broadrcaster.publish(command_third_degree, int(movement))
                time.sleep(speed_factor)
                print("--command send")

    if(fourth_degree == fourth_degree_old):
        print('sending command in chanel : {0} the command is : {1}'.format(
            str(command_fourth_degree), str(fourth_degree)))
        broadrcaster.publish(command_fourth_degree, int(fourth_degree))
        time.sleep(speed_factor)
        print("--command send")
    else:
        if(fourth_degree < fourth_degree_old):
            for movement in range(fourth_degree, fourth_degree_old, 1):
                print('sending command in chanel : {0} the command is : {1}'.format(
                    str(command_fourth_degree), str(movement)))
                broadrcaster.publish(command_fourth_degree, int(movement))
                time.sleep(speed_factor)
                print("--command send")
        elif(fourth_degree < fourth_degree_old):
            for movement in range(fourth_degree_old, fourth_degree, 1):
                print('sending command in chanel : {0} the command is : {1}'.format(
                    str(command_fourth_degree), str(movement)))
                broadrcaster.publish(command_fourth_degree, int(movement))
                time.sleep(speed_factor)
                print("--command send")

    if(fifth_degree == fifth_degree_old):
        print('sending command in chanel : {0} the command is : {1}'.format(
            str(command_fifth_degree), str(fifth_degree)))
        broadrcaster.publish(command_fifth_degree, int(fifth_degree))
        time.sleep(speed_factor)
        print("--command send")
    else:
        if(fifth_degree < fifth_degree_old):
            for movement in range(fifth_degree, fifth_degree_old, 1):
                print('sending command in chanel : {0} the command is : {1}'.format(
                    str(command_fifth_degree), str(movement)))
                broadrcaster.publish(command_fifth_degree, int(movement))
                time.sleep(speed_factor)
                print("--command send")
        elif(fifth_degree < fifth_degree_old):
            for movement in range(fifth_degree_old, fifth_degree, 1):
                print('sending command in chanel : {0} the command is : {1}'.format(
                    str(command_fifth_degree), str(movement)))
                broadrcaster.publish(command_fifth_degree, int(movement))
                time.sleep(speed_factor)
                print("--command send")

    if(claw == claw_old):
        print('sending command in chanel : {0} the command is : {1}'.format(
            str(command_claw), str(claw)))
        broadrcaster.publish(command_claw, int(claw))
        time.sleep(speed_factor)
        print("--command send")
    else:
        if(claw < claw_old):
            for movement in range(claw, claw_old, 1):
                print('sending command in chanel : {0} the command is : {1}'.format(
                    str(command_claw), str(movement)))
                broadrcaster.publish(command_claw, int(movement))
                time.sleep(speed_factor)
            print("--command send")
        elif(claw < claw_old):
            for movement in range(claw_old, claw, 1):
                print('sending command in chanel : {0} the command is : {1}'.format(
                    str(command_claw), str(movement)))
                broadrcaster.publish(command_claw, int(movement))
                time.sleep(speed_factor)
                print("--command send")

    first_degree_old = first_degree
    second_degree_old = second_degree
    third_degree_old = third_degree
    fourth_degree_old = fourth_degree
    fifth_degree_old = fifth_degree
    claw_old = claw
    return


def initial_state_witout_object():
    print("-> prepaing for initial state")
    global first_degree, second_degree, third_degree, fourth_degree, fifth_degree, claw
    first_degree = 61
    second_degree = 5
    third_degree = 4
    fourth_degree = 53
    fifth_degree = 11
    claw = 79
    update_position()
    print("----task compleated")


def second_state_witout_object():
    print("-> prepaing for second state")
    global first_degree, second_degree, third_degree, fourth_degree, fifth_degree, claw
    second_degree = 44
    update_position()
    print("----task compleated")


def third_state_witout_object():
    print("-> prepaing for third state")
    global first_degree, second_degree, third_degree, fourth_degree, fifth_degree, claw
    claw = 0
    update_position()
    print("----task compleated")


def fourth_state_witout_object():
    print("-> prepaing for fourth state")
    global first_degree, second_degree, third_degree, fourth_degree, fifth_degree, claw
    third_degree = 100
    update_position()
    print("----task compleated")


def fifth_state_witout_object():
    print("-> prepaing for fifth state")
    global first_degree, second_degree, third_degree, fourth_degree, fifth_degree, claw
    claw = 91
    update_position()
    print("----task compleated")


print("starting auto script")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

broadrcaster = get_broadrcaster()


initial_state_witout_object()
second_state_witout_object()
third_state_witout_object()
fourth_state_witout_object()
fifth_state_witout_object()
