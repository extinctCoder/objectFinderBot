import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

motor_a_1 = 31
motor_a_2 = 33
motor_b_1 = 35
motor_b_2 = 37

motor_a_pwm = 36
motor_b_pwm = 38


command_motor_direction = "objectFinderBot/motor/command/direction"
command_motor_speed = "objectFinderBot/motor/command/speed"
topic = "objectFinderBot/motor/command/#"

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(motor_a_1, GPIO.OUT)
GPIO.setup(motor_a_2, GPIO.OUT)
GPIO.setup(motor_b_1, GPIO.OUT)
GPIO.setup(motor_b_2, GPIO.OUT)
GPIO.setup(motor_a_pwm, GPIO.OUT)
GPIO.setup(motor_b_pwm, GPIO.OUT)

pwm_a = GPIO.PWM(motor_a_pwm, 5000)
pwm_b = GPIO.PWM(motor_b_pwm, 5000)
pwm_a.start(0)
pwm_b.start(0)


def forward():
    GPIO.output(motor_a_1, GPIO.HIGH)
    GPIO.output(motor_a_2, GPIO.LOW)
    GPIO.output(motor_b_1, GPIO.HIGH)
    GPIO.output(motor_b_2, GPIO.LOW)
    return


def backward():
    GPIO.output(motor_a_1, GPIO.LOW)
    GPIO.output(motor_a_2, GPIO.HIGH)
    GPIO.output(motor_b_1, GPIO.LOW)
    GPIO.output(motor_b_2, GPIO.HIGH)
    return


def left():
    GPIO.output(motor_a_1, GPIO.HIGH)
    GPIO.output(motor_a_2, GPIO.LOW)
    GPIO.output(motor_b_1, GPIO.LOW)
    GPIO.output(motor_b_2, GPIO.HIGH)
    return


def right():
    GPIO.output(motor_a_1, GPIO.LOW)
    GPIO.output(motor_a_2, GPIO.HIGH)
    GPIO.output(motor_b_1, GPIO.HIGH)
    GPIO.output(motor_b_2, GPIO.LOW)
    return


def stop():
    GPIO.output(motor_a_1, GPIO.LOW)
    GPIO.output(motor_a_2, GPIO.LOW)
    GPIO.output(motor_b_1, GPIO.LOW)
    GPIO.output(motor_b_2, GPIO.LOW)
    return


def change_speed(speed):
    pwm_a.ChangeDutyCycle(speed)
    pwm_b.ChangeDutyCycle(speed)
    return


def on_message(client, userdata, message):
    print(message)
    print("xxxx")
    if(message.topic == command_motor_speed):
        change_speed(int(str(message.payload.decode("utf-8"))))
    elif(message.topic == command_motor_direction):
        if(int(str(message.payload.decode("utf-8"))) == 0):
            forward()
            print("forward")
        elif(int(str(message.payload.decode("utf-8"))) == 1):
            left()
            print("left")
        elif(int(str(message.payload.decode("utf-8"))) == 2):
            backward()
            print("backward")
        elif(int(str(message.payload.decode("utf-8"))) == 3):
            right()
            print("right")
        elif(int(str(message.payload.decode("utf-8"))) == 4):
            stop()
            print("stop")
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


try:
    print("Wellcome to mqtt broker rover runner script")
    print("Creating new instance of mqtt client")
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    # client.on_log = on_log
    print("Connecting to mqtt broker")
    client.connect("192.168.0.117")
    client.loop_forever()

except KeyboardInterrupt:
    pwm_a.stop()
    pwm_b.stop()
    GPIO.cleanup()
