from adafruit_servokit import ServoKit
import time

time_sleep = .2

servo_num = 14

if_loop = 0
fix_angle = 110

max = 180
min = 50

kit = ServoKit(channels=16)

if if_loop == 0:

    kit.servo[servo_num].angle = fix_angle

else:
    while 1:
        for i in range(min, max, 1):
            kit.servo[servo_num].angle = i
            print(i)
            time.sleep(time_sleep)
        time.sleep(time_sleep)
        for i in range(max, min, -1):
            kit.servo[servo_num].angle = i
            print(i)
            time.sleep(time_sleep)
        time.sleep(time_sleep)
