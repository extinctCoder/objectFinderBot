import time

import json
from tkinter import *
import paho.mqtt.client as mqtt
# Define Variables
MQTT_BROKER = "192.168.0.117"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 6000

speed_factor = .2
speed_limit = 5
broadrcaster = None

with open('servoPos.json', 'r') as servoPos:
    data = servoPos.read()

obj = json.loads(data)


first_degree_old = int(obj['servoOne'])
second_degree_old = int(obj['servoTwo'])
third_degree_old = int(obj['servoThree'])
fourth_degree_old = int(obj['servoFour'])
fifth_degree_old = int(obj['servoFive'])
claw_old = int(obj['servoSix'])

first_degree = 0
second_degree = 0
third_degree = 0
fourth_degree = 0
fifth_degree = 0
claw = 0


first_degree_current = 0
second_degree_current = 0
third_degree_current = 0
fourth_degree_current = 0
fifth_degree_current = 0
claw_current = 0

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
    # broadrcaster.on_log = on_log
    print("connecting with the server")
    broadrcaster.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
    return broadrcaster


def update_position():
    global speed_factor
    global first_degree, second_degree, third_degree, fourth_degree, fifth_degree, claw
    global first_degree_current, second_degree_current, third_degree_current, fourth_degree_current, fifth_degree_current, claw_current
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

    print("> prepring to transmit data. please wait ....")

    print("preparing to bot commmand")
    for i in range(0, speed_limit, 1):
        time.sleep(speed_factor)
        print('\r', i, end=" ")
    print(" ")

    if(claw < claw_old):
        for movement in range(claw_old, claw, -1):
            print('sending command in chanel : {0} the command is : {1}'.format(
                str(command_claw), str(movement)))
            claw_current = movement
            claw_old = movement
            broadrcaster.publish(command_claw, int(movement))
            time.sleep(speed_factor)
        print("--command send")
    elif(claw > claw_old):
        for movement in range(claw_old, claw, 1):
            print('sending command in chanel : {0} the command is : {1}'.format(
                str(command_claw), str(movement)))
            claw_current = movement
            claw_old = movement
            broadrcaster.publish(command_claw, int(movement))
            time.sleep(speed_factor)
            print("--command send")

    print('sending command in chanel : {0} the command is : {1}'.format(
        str(command_claw), str(claw)))
    claw_current = claw
    claw_old = claw
    broadrcaster.publish(command_claw, int(claw))
    time.sleep(speed_factor)
    print("--command send")

    print("preparing to bot commmand")
    for i in range(0, speed_limit, 1):
        time.sleep(speed_factor)
        print('\r', i, end=" ")
    print(" ")

    if(fifth_degree < fifth_degree_old):
        for movement in range(fifth_degree_old, fifth_degree, -1):
            print('sending command in chanel : {0} the command is : {1}'.format(
                str(command_fifth_degree), str(movement)))
            fifth_degree_current = movement
            fifth_degree_old = movement
            broadrcaster.publish(command_fifth_degree, int(movement))
            time.sleep(speed_factor)
            print("--command send")
    elif(fifth_degree > fifth_degree_old):
        for movement in range(fifth_degree_old, fifth_degree, 1):
            print('sending command in chanel : {0} the command is : {1}'.format(
                str(command_fifth_degree), str(movement)))
            fifth_degree_current = movement
            fifth_degree_old = movement
            broadrcaster.publish(command_fifth_degree, int(movement))
            time.sleep(speed_factor)
            print("--command send")

    print('sending command in chanel : {0} the command is : {1}'.format(
        str(command_fifth_degree), str(fifth_degree)))
    fifth_degree_current = fifth_degree
    fifth_degree_old = fifth_degree
    broadrcaster.publish(command_fifth_degree, int(fifth_degree))
    time.sleep(speed_factor)
    print("--command send")

    print("preparing to bot commmand")
    for i in range(0, speed_limit, 1):
        time.sleep(speed_factor)
        print('\r', i, end=" ")
    print(" ")

    if(fourth_degree < fourth_degree_old):
        for movement in range(fourth_degree_old, fourth_degree, -1):
            print('sending command in chanel : {0} the command is : {1}'.format(
                str(command_fourth_degree), str(movement)))
            fourth_degree_current = movement
            fourth_degree_old = movement
            broadrcaster.publish(command_fourth_degree, int(movement))
            time.sleep(speed_factor)
            print("--command send")
    elif(fourth_degree > fourth_degree_old):
        for movement in range(fourth_degree_old, fourth_degree, 1):
            print('sending command in chanel : {0} the command is : {1}'.format(
                str(command_fourth_degree), str(movement)))
            fourth_degree_current = movement
            fourth_degree_old = movement
            broadrcaster.publish(command_fourth_degree, int(movement))
            time.sleep(speed_factor)
            print("--command send")

    print('sending command in chanel : {0} the command is : {1}'.format(
        str(command_fourth_degree), str(fourth_degree)))
    fourth_degree_current = fourth_degree
    fourth_degree_old = fourth_degree
    broadrcaster.publish(command_fourth_degree, int(fourth_degree))
    time.sleep(speed_factor)
    print("--command send")

    print("preparing to bot commmand")
    for i in range(0, speed_limit, 1):
        time.sleep(speed_factor)
        print('\r', i, end=" ")
    print(" ")

    if(third_degree < third_degree_old):
        for movement in range(third_degree_old, third_degree, -1):
            print('sending command in chanel : {0} the command is : {1}'.format(
                str(command_third_degree), str(movement)))
            third_degree_current = movement
            third_degree_old = movement
            broadrcaster.publish(command_third_degree, int(movement))
            time.sleep(speed_factor)
            print("--command send")
    elif(third_degree > third_degree_old):
        for movement in range(third_degree_old, third_degree, 1):
            print('sending command in chanel : {0} the command is : {1}'.format(
                str(command_third_degree), str(movement)))
            third_degree_current = movement
            third_degree_old = movement
            broadrcaster.publish(command_third_degree, int(movement))
            time.sleep(speed_factor)
            print("--command send")

    print('sending command in chanel : {0} the command is : {1}'.format(
        str(command_third_degree), str(third_degree)))
    third_degree_current = third_degree
    third_degree_old = third_degree
    broadrcaster.publish(command_third_degree, int(third_degree))
    time.sleep(speed_factor)
    print("--command send")

    print("preparing to bot commmand")
    for i in range(0, speed_limit, 1):
        time.sleep(speed_factor)
        print('\r', i, end=" ")
    print(" ")

    '''if(second_degree < second_degree_old):

        for movement in range(second_degree_old, second_degree, -1):
            print('sending command in chanel : {0} the command is : {1}'.format(
                str(command_second_degree), str(movement)))
            second_degree_current = movement
            second_degree_old = movement
            broadrcaster.publish(command_second_degree, int(movement))
            time.sleep(speed_factor*3)
            print("--command send")
    elif(second_degree > second_degree_old):
        for movement in range(second_degree_old, second_degree, 1):
            print('sending command in chanel : {0} the command is : {1}'.format(
                str(command_second_degree), str(movement)))
            second_degree_current = movement
            second_degree_old = movement
            broadrcaster.publish(command_second_degree, int(movement))
            time.sleep(speed_factor*3)
            print("--command send")

    print('sending command in chanel : {0} the command is : {1}'.format(
        str(command_second_degree), str(second_degree)))
    second_degree_current = second_degree
    second_degree_old = second_degree
    broadrcaster.publish(command_second_degree, int(second_degree))
    time.sleep(speed_factor*3)
    print("--command send")

    print("preparing to bot commmand")
    for i in range(0, speed_limit, 1):
        time.sleep(speed_factor)
        print('\r', i, end=" ")
    print(" ")

    if(first_degree < first_degree_old):
        for movement in range(first_degree_old, first_degree, -1):
            print('sending command in chanel : {0} the command is : {1}'.format(
                str(command_first_degree), str(movement)))
            first_degree_current = movement
            first_degree_old = movement
            broadrcaster.publish(command_first_degree, int(movement))
            time.sleep(speed_factor)
            print("--command send")
    elif(first_degree > first_degree_old):
        for movement in range(first_degree_old, first_degree, 1):
            print('sending command in chanel : {0} the command is : {1}'.format(
                str(command_first_degree), str(movement)))
            first_degree_current = movement
            first_degree_old = movement
            broadrcaster.publish(command_first_degree, int(movement))
            time.sleep(speed_factor)
            print("--command send")'''

    print('sending command in chanel : {0} the command is : {1}'.format(
        str(command_first_degree), str(first_degree)))
    first_degree_current = first_degree
    first_degree_old = first_degree
    broadrcaster.publish(command_first_degree, int(first_degree))
    time.sleep(speed_factor)
    print("--command send")

    print("> data transmission successfull ....")
    first_degree_old = first_degree
    second_degree_old = second_degree
    third_degree_old = third_degree
    fourth_degree_old = fourth_degree
    fifth_degree_old = fifth_degree
    claw_old = claw

    print("preparing to bot commmand")
    for i in range(0, speed_limit, 1):
        time.sleep(speed_factor)
        print('\r', i, end=" ")
    print(" ")

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
    return


def backup_data_into_db():
    print("Writing last known servo position into database")
    with open('servoPos.json', 'w') as servoPos:
        print('last known angle of the servo no. 1 is : {0}'.format(str(
            first_degree_current)))
        print('last known angle of the servo no. 2 is : {0}'.format(str(
            second_degree_current)))
        print('last known angle of the servo no. 3 is : {0}'.format(str(
            third_degree_current)))
        print('last known angle of the servo no. 4 is : {0}'.format(str(
            fourth_degree_current)))
        print('last known angle of the servo no. 5 is : {0}'.format(str(
            fifth_degree_current)))
        print('last known angle of the servo no. 6 is : {0}'.format(str(
            claw_current)))
        obj['servoOne'] = first_degree_current
        obj['servoTwo'] = second_degree_current
        obj['servoThree'] = third_degree_current
        obj['servoFour'] = fourth_degree_current
        obj['servoFive'] = fifth_degree_current
        obj['servoSix'] = claw_current
        json.dump(obj, servoPos)
    return


def initial_state_witout_object():
    print("-> prepaing for initial_state_witout_object state")
    global first_degree, second_degree, third_degree, fourth_degree, fifth_degree, claw
    third_degree = 0
    fourth_degree = 0
    fifth_degree = 0
    claw = 100
    update_position()
    print("----task compleated")


def ready_to_pickup_state():
    print("-> prepaing for ready_to_pickup_state state")
    global first_degree, second_degree, third_degree, fourth_degree, fifth_degree, claw
    third_degree = 100
    fourth_degree = 50
    fifth_degree = 10
    claw = 0
    update_position()
    print("----task compleated")


def pickup_and_retrive_state():
    print("-> prepaing for pickup_and_retrive_state state")
    global first_degree, second_degree, third_degree, fourth_degree, fifth_degree, claw
    fourth_degree = 0
    fifth_degree = 0
    claw = 100
    update_position()
    print("----task compleated")


'''

def remove_object_state():
    print("-> prepaing for fourth state")
    global first_degree, second_degree, third_degree, fourth_degree, fifth_degree, claw
    third_degree = 100
    fourth_degree = 50
    fifth_degree = 10
    update_position()
    claw = 0
    update_position()
    third_degree = 0
    update_position()
    # third_degree = 0
    # fourth_degree = 0
    # fifth_degree = 0
    claw = 100
    update_position()
    print("----task compleated")




def fifth_state_witout_object():
    print("-> prepaing for fifth state")
    global first_degree, second_degree, third_degree, fourth_degree, fifth_degree, claw
    claw = 91
    update_position()
    print("----task compleated")
'''


def run():
    try:
        print("starting auto script")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)

        broadrcaster = get_broadrcaster()

        print("connnection established")
        print("syncing servopositions from the data base")

        print('last known angle of the servo no. 1 is : {0}'.format(str(
            first_degree_old)))
        print('last known angle of the servo no. 2 is : {0}'.format(str(
            second_degree_old)))
        print('last known angle of the servo no. 3 is : {0}'.format(str(
            third_degree_old)))
        print('last known angle of the servo no. 4 is : {0}'.format(str(
            fourth_degree_old)))
        print('last known angle of the servo no. 5 is : {0}'.format(str(
            fifth_degree_old)))
        print('last known angle of the servo no. 6 is : {0}'.format(str(
            claw_old)))

        first_degree = first_degree_old
        second_degree = second_degree_old
        third_degree = third_degree_old
        fourth_degree = fourth_degree_old
        fifth_degree = fifth_degree_old
        claw = claw_old

        time.sleep(speed_factor)
        update_position()
        for i in range(0, 1):
            initial_state_witout_object()
            time.sleep(speed_factor*speed_limit)
            ready_to_pickup_state()
            time.sleep(speed_factor*speed_limit)
            pickup_and_retrive_state()
            time.sleep(speed_factor*speed_limit)
    except KeyboardInterrupt:
        print("unexpected user input detected. enabling emergency mode ....!!!!")

    finally:
        # initial_state_witout_object()
        backup_data_into_db()


if __name__ == '__main__':
    try:
        print("starting auto script")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)

        broadrcaster = get_broadrcaster()

        print("connnection established")
        print("syncing servopositions from the data base")

        print('last known angle of the servo no. 1 is : {0}'.format(str(
            first_degree_old)))
        print('last known angle of the servo no. 2 is : {0}'.format(str(
            second_degree_old)))
        print('last known angle of the servo no. 3 is : {0}'.format(str(
            third_degree_old)))
        print('last known angle of the servo no. 4 is : {0}'.format(str(
            fourth_degree_old)))
        print('last known angle of the servo no. 5 is : {0}'.format(str(
            fifth_degree_old)))
        print('last known angle of the servo no. 6 is : {0}'.format(str(
            claw_old)))

        first_degree = first_degree_old
        second_degree = second_degree_old
        third_degree = third_degree_old
        fourth_degree = fourth_degree_old
        fifth_degree = fifth_degree_old
        claw = claw_old

        time.sleep(speed_factor)
        update_position()
        for i in range(0, 1):
            initial_state_witout_object()
            time.sleep(speed_factor*speed_limit)
            ready_to_pickup_state()
            time.sleep(speed_factor*speed_limit)
            pickup_and_retrive_state()
            time.sleep(speed_factor*speed_limit)
    except KeyboardInterrupt:
        print("unexpected user input detected. enabling emergency mode ....!!!!")

    finally:
        # initial_state_witout_object()
        backup_data_into_db()
