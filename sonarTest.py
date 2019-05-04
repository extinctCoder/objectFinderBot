import RPi.GPIO as GPIO
import time

import paho.mqtt.client as mqtt

MQTT_BROKER = "192.168.0.117"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 6000

command_sonar_data = "objectFinderBot/motor/command/sonar"

GPIO.setmode(GPIO.BOARD)

GPIO_TRIGGER = 11
GPIO_ECHO = 13

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def get_broadrcaster():
    global broadrcaster
    broadrcaster = mqtt.Client()
    print("connecting with the server")
    broadrcaster.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
    print("Server connected")
    return broadrcaster


def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance


if __name__ == '__main__':
    try:
        broadrcaster = get_broadrcaster()
        while True:

            dist = distance()
            print("Measured Distance = %.1f cm" % dist)
            broadrcaster.publish(command_sonar_data, int(dist))
            time.sleep(.02)

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
