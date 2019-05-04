from __future__ import division
import paho.mqtt.client as mqtt
from adafruit_servokit import ServoKit
import time
import json

topic = "objectFinderBot/hand/command/#"


kit = ServoKit(channels=16)


first_degree_min = 0
first_degree_max = 180

second_degree_min = 0
second_degree_max = 35

third_degree_min = 15
third_degree_max = 180

fourth_degree_min = 0
fourth_degree_max = 180

fifth_degree_min = 0
fifth_degree_max = 180

claw_min = 50
claw_max = 120

command_first_degree = "objectFinderBot/hand/command/first_degree"
command_second_degree = "objectFinderBot/hand/command/second_degree"
command_third_degree = "objectFinderBot/hand/command/third_degree"
command_fourth_degree = "objectFinderBot/hand/command/fourth_degree"
command_fifth_degree = "objectFinderBot/hand/command/fifth_degree"
command_claw = "objectFinderBot/hand/command/claw"


with open('servoPos.json', 'r') as servoPos:
    data = servoPos.read()

obj = json.loads(data)


servo_postion = [int(obj['servoOne']), int(obj['servoTwo']), int(obj['servoThree']), int(
    obj['servoFour']), int(obj['servoFive']), int(obj['servoSix'])]


def syncServo(servo_flag, position):
    global servo_postion, kit

    speed_factor = .01
    print('writing the angle : {0} in servo no : {1}'.format(
        str(position), str(servo_flag+1)))
    if(servo_flag != 0):
        kit.servo[servo_flag].angle = position
    time.sleep(speed_factor)
    '''if(position == servo_postion[servo_flag] or servo_postion[servo_flag] == -1):
        print('writing the angle : {0} in servo no : {1}'.format(
            str(position), str(servo_flag+1)))
        kit.servo[servo_flag].angle = position
        time.sleep(speed_factor)
    elif(position == servo_postion[servo_flag] + 1 or position == servo_postion[servo_flag] - 1):
        print('writing the angle : {0} in servo no : {1}'.format(
            str(position), str(servo_flag+1)))
        kit.servo[servo_flag].angle = position
        time.sleep(speed_factor)
    else:
        if(position < servo_postion[servo_flag]):
            print("position < servo_postion[servo_flag]")
            for movement in range(servo_postion[servo_flag], servo_postion[servo_flag], -1):
                print('writing the angle : {0} in servo no : {1}'.format(
                    str(movement), str(servo_flag+1)))
                kit.servo[servo_flag].angle = movement
                time.sleep(speed_factor)
        elif(position > servo_postion[servo_flag]):
            print("position > servo_postion[servo_flag]")
            for movement in range(servo_postion[servo_flag], servo_postion[servo_flag], 1):
                print('writing the angle : {0} in servo no : {1}'.format(
                    str(movement), str(servo_flag+1)))
                kit.servo[servo_flag].angle = movement
                time.sleep(speed_factor)'''
    servo_postion[servo_flag] = position
    return


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
        syncServo(0, angle_value)
    elif(message.topic == command_second_degree):
        angle_value = map_value(int(str(message.payload.decode(
            "utf-8"))), second_degree_max, second_degree_min)
        print("command_second_degree : {}".format(angle_value))
        syncServo(1, angle_value)
    elif(message.topic == command_third_degree):
        angle_value = map_value(
            int(str(message.payload.decode("utf-8"))), third_degree_max, third_degree_min)
        print("command_third_degree : {}".format(angle_value))
        syncServo(2, angle_value)
    elif(message.topic == command_fourth_degree):
        angle_value = map_value(int(str(message.payload.decode(
            "utf-8"))), fourth_degree_max, fourth_degree_min)
        print("command_fourth_degree : {}".format(angle_value))
        syncServo(3, angle_value)
    elif(message.topic == command_fifth_degree):
        angle_value = map_value(
            int(str(message.payload.decode("utf-8"))), fifth_degree_max, fifth_degree_min)
        print("command_fifth_degree : {}".format(angle_value))
        syncServo(4, angle_value)
    elif(message.topic == command_claw):
        angle_value = map_value(
            int(str(message.payload.decode("utf-8"))), claw_max, claw_min)
        print("command_claw : {}".format(angle_value))
        syncServo(5, angle_value)
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


if __name__ == '__main__':
    try:
        print("Wellcome to mqtt broker subscribe script")
        print("Creating new instance of mqtt client")
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        # client.on_log = on_log
        print("Connecting to mqtt broker")
        client.connect("192.168.0.117")
        print("connnection established")
        print("syncing servopositions from the data base")

        for servo in range(0, 6, 1):
            syncServo(servo, servo_postion[servo])
            print('last known angle of the servo no. {0} is : {1}'.format(
                str(servo+1), str(servo_postion[servo])))
            print("please wait while we are prepaire robo hand")
            time.sleep(2)
        client.loop_forever()

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        global obj, servo_postion
        print("Writing last known servo position into database")
        with open('servoPos.json', 'w') as servoPos:
            obj['servoOne'] = servo_postion[0]
            obj['servoTwo'] = servo_postion[1]
            obj['servoThree'] = servo_postion[2]
            obj['servoFour'] = servo_postion[3]
            obj['servoFive'] = servo_postion[4]
            obj['servoSix'] = servo_postion[5]
            json.dump(obj, servoPos)
