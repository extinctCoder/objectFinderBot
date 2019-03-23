from __future__ import division
import time

import Adafruit_PCA9685

import logging

logging.basicConfig(level=logging.DEBUG)

pwm = Adafruit_PCA9685.PCA9685()

servo_min = 150  # Min pulse length out of 4096
servo_max = 250  # Max pulse length out of 4096

pwm.set_pwm_freq(60)

print('Moving servo on channel 0, press Ctrl-C to quit...')

'''while True:
    pwm.set_pwm(0, 0, servo_min)
    time.sleep(2)
    pwm.set_pwm(0, 0, servo_max)
    time.sleep(2)'''
pwm.set_pwm(0, 0, 100)
