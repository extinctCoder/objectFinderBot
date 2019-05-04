#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)

# setup gpio for echo & trig
echopin = [11, 19]
trigpin = [13, 21]

limit = 1

for j in range(limit):
    GPIO.setup(trigpin[j], GPIO.OUT)
    GPIO.setup(echopin[j], GPIO.IN)
    print(j, echopin[j], trigpin[j])
    print(" ")


# Get reading from HC-SR04
def ping(echo, trig):

    GPIO.output(trig, False)
    # Allow module to settle
    print("time.sleep(0.5)")
    time.sleep(0.5)
    # Send 10us pulse to trigger
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)
    pulse_start = time.time()

    # save StartTime
    while GPIO.input(echo) == 0:
        pulse_start = time.time()

    # save time of arrival
    while GPIO.input(echo) == 1:
        pulse_end = time.time()

    # time difference between start and arrival
    pulse_duration = pulse_end - pulse_start
    # mutiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = pulse_duration * 17150

    distance = round(distance, 2)

    return distance


print(" press Ctrl+c to stop program ")
try:
    while True:
        for j in range(limit):
            distance = ping(echopin[j], trigpin[j])
            print("sensor", j+1, ": ", distance, "cm \n")
        print("wait")
        time.sleep(.1)

except KeyboardInterrupt:
    print("keyboard interrupt detected")
