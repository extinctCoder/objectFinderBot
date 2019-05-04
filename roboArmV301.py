from adafruit_servokit import ServoKit
import time
kit = ServoKit(channels=16)

kit.servo[5].angle = 50
time.sleep(1)
kit.servo[4].angle = 0
time.sleep(1)
kit.servo[3].angle = 0
time.sleep(1)
kit.servo[2].angle = 15
time.sleep(1)
kit.servo[1].angle = 15
time.sleep(1)
kit.servo[0].angle = 60
time.sleep(1)
