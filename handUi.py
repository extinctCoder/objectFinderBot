import time
from tkinter import *
import paho.mqtt.client as mqtt
# Define Variables
MQTT_BROKER = "192.168.0.104"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 6000

hand_speed_factor = 0.00
broadrcaster = None

max_inc = 100.00
min_dec = 0.00

speed_first_degree = 0.00
speed_second_degree = 0.00
speed_third_degree = 0.00
speed_fourth_degree = 0.00
speed_fifth_degree = 0.00
speed_claw = 0.00

command_first_degree = "objectFinderBot/hand/command/first_degree"
command_second_degree = "objectFinderBot/hand/command/second_degree"
command_third_degree = "objectFinderBot/hand/command/third_degree"
command_fourth_degree = "objectFinderBot/hand/command/fourth_degree"
command_fifth_degree = "objectFinderBot/hand/command/fifth_degree"
command_claw = "objectFinderBot/hand/command/claw"


def button_state_toggle():
    first_degree_inc_update_btn.config(state=DISABLED)
    first_degree_dec_update_btn.config(state=DISABLED)
    second_degree_inc_update_btn.config(state=DISABLED)
    second_degree_dec_update_btn.config(state=DISABLED)
    third_degree_inc_update_btn.config(state=DISABLED)
    third_degree_dec_update_btn.config(state=DISABLED)
    fourth_degree_inc_update_btn.config(state=DISABLED)
    fourth_degree_dec_update_btn.config(state=DISABLED)
    fifth_degree_inc_update_btn.config(state=DISABLED)
    fifth_degree_dec_update_btn.config(state=DISABLED)
    claw_inc_update_btn.config(state=DISABLED)
    claw_dec_update_btn.config(state=DISABLED)
    speed_update_scale.config(state=DISABLED)
    time.sleep(.5)
    first_degree_inc_update_btn.config(state=ACTIVE)
    first_degree_dec_update_btn.config(state=ACTIVE)
    second_degree_inc_update_btn.config(state=ACTIVE)
    second_degree_dec_update_btn.config(state=ACTIVE)
    third_degree_inc_update_btn.config(state=ACTIVE)
    third_degree_dec_update_btn.config(state=ACTIVE)
    fourth_degree_inc_update_btn.config(state=ACTIVE)
    fourth_degree_dec_update_btn.config(state=ACTIVE)
    fifth_degree_inc_update_btn.config(state=ACTIVE)
    fifth_degree_dec_update_btn.config(state=ACTIVE)
    claw_inc_update_btn.config(state=ACTIVE)
    claw_dec_update_btn.config(state=ACTIVE)
    speed_update_scale.config(state=ACTIVE)
    return


def get_broadrcaster():
    global broadrcaster
    print("starting the mqtt calibration vroadcust module")
    broadrcaster = mqtt.Client()
    print("connecting with the server")
    broadrcaster.connect(MQTT_BROKER, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
    return broadrcaster


def distroy_broadrcaster():
    global broadrcaster
    broadrcaster.loop_stop()
    broadrcaster.disconnect()
    return


def first_degree_inc_update_func():
    global broadrcaster, speed_first_degree, hand_speed_factor, max_inc
    if(speed_first_degree + hand_speed_factor <= max_inc):
        speed_first_degree += hand_speed_factor
        pass
    broadrcaster.publish(command_first_degree, int(speed_first_degree))
    first_degree_txt.config(text=str(speed_first_degree))
    button_state_toggle()
    return


def first_degree_dec_update_func():
    global broadrcaster, speed_first_degree, hand_speed_factor, min_dec
    if(speed_first_degree - hand_speed_factor >= min_dec):
        speed_first_degree -= hand_speed_factor
        pass
    broadrcaster.publish(command_first_degree, int(speed_first_degree))
    first_degree_txt.config(text=str(speed_first_degree))
    button_state_toggle()
    return


def second_degree_inc_update_func():
    global broadrcaster, speed_second_degree, hand_speed_factor, max_inc
    if(speed_second_degree + hand_speed_factor <= max_inc):
        speed_second_degree += hand_speed_factor
        pass
    broadrcaster.publish(command_second_degree, int(speed_second_degree))
    second_degree_txt.config(text=str(speed_second_degree))
    button_state_toggle()
    return


def second_degree_dec_update_func():
    global broadrcaster, speed_second_degree, hand_speed_factor, min_dec
    if(speed_second_degree - hand_speed_factor >= min_dec):
        speed_second_degree -= hand_speed_factor
        pass
    broadrcaster.publish(command_second_degree, int(speed_second_degree))
    second_degree_txt.config(text=str(speed_second_degree))
    button_state_toggle()
    return


def third_degree_inc_update_func():
    global broadrcaster, speed_third_degree, hand_speed_factor, max_inc
    if(speed_third_degree + hand_speed_factor <= max_inc):
        speed_third_degree += hand_speed_factor
        pass
    broadrcaster.publish(command_third_degree, int(speed_third_degree))
    third_degree_txt.config(text=str(speed_third_degree))
    button_state_toggle()
    return


def third_degree_dec_update_func():
    global broadrcaster, speed_third_degree, hand_speed_factor, min_dec
    if(speed_third_degree - hand_speed_factor >= min_dec):
        speed_third_degree -= hand_speed_factor
        pass
    broadrcaster.publish(command_third_degree, int(speed_third_degree))
    third_degree_txt.config(text=str(speed_third_degree))
    button_state_toggle()
    return


def fourth_degree_inc_update_func():
    global broadrcaster, speed_fourth_degree, hand_speed_factor, max_inc
    if(speed_fourth_degree + hand_speed_factor <= max_inc):
        speed_fourth_degree += hand_speed_factor
        pass
    broadrcaster.publish(command_fourth_degree, int(speed_fourth_degree))
    fourth_degree_txt.config(text=str(speed_fourth_degree))
    button_state_toggle()
    return


def fourth_degree_dec_update_func():
    global broadrcaster, speed_fourth_degree, hand_speed_factor, min_dec
    if(speed_fourth_degree - hand_speed_factor >= min_dec):
        speed_fourth_degree -= hand_speed_factor
        pass
    broadrcaster.publish(command_fourth_degree, int(speed_fourth_degree))
    fourth_degree_txt.config(text=str(speed_fourth_degree))
    button_state_toggle()
    return


def fifth_degree_inc_update_func():
    global broadrcaster, speed_fifth_degree, hand_speed_factor, max_inc
    if(speed_fifth_degree + hand_speed_factor <= max_inc):
        speed_fifth_degree += hand_speed_factor
        pass
    broadrcaster.publish(command_fifth_degree, int(speed_fifth_degree))
    fifth_degree_txt.config(text=str(speed_fifth_degree))
    button_state_toggle()
    return


def fifth_degree_dec_update_func():
    global broadrcaster, speed_fifth_degree, hand_speed_factor, min_dec
    if(speed_fifth_degree - hand_speed_factor >= min_dec):
        speed_fifth_degree -= hand_speed_factor
        pass
    broadrcaster.publish(command_fifth_degree, int(speed_fifth_degree))
    fifth_degree_txt.config(text=str(speed_fifth_degree))
    button_state_toggle()
    return


def claw_inc_update_func():
    global broadrcaster, speed_claw, hand_speed_factor, max_inc
    if(speed_claw + hand_speed_factor <= max_inc):
        speed_claw += hand_speed_factor
        pass
    broadrcaster.publish(command_claw, int(speed_claw))
    claw_txt.config(text=str(speed_claw))
    button_state_toggle()
    return


def claw_dec_update_func():
    global broadrcaster, speed_claw, hand_speed_factor, min_dec
    if(speed_claw - hand_speed_factor >= min_dec):
        speed_claw -= hand_speed_factor
        pass
    broadrcaster.publish(command_claw, int(speed_claw))
    claw_txt.config(text=str(speed_claw))
    button_state_toggle()
    return


def sync_func():
    global broadrcaster
    global speed_first_degree
    global speed_second_degree
    global speed_third_degree
    global speed_fourth_degree
    global speed_fifth_degree
    global speed_claw

    global hand_speed_factor

    first_degree_inc_update_btn.config(state=DISABLED)
    first_degree_dec_update_btn.config(state=DISABLED)
    second_degree_inc_update_btn.config(state=DISABLED)
    second_degree_dec_update_btn.config(state=DISABLED)
    third_degree_inc_update_btn.config(state=DISABLED)
    third_degree_dec_update_btn.config(state=DISABLED)
    fourth_degree_inc_update_btn.config(state=DISABLED)
    fourth_degree_dec_update_btn.config(state=DISABLED)
    fifth_degree_inc_update_btn.config(state=DISABLED)
    fifth_degree_dec_update_btn.config(state=DISABLED)
    claw_inc_update_btn.config(state=DISABLED)
    claw_dec_update_btn.config(state=DISABLED)
    speed_update_scale.config(state=DISABLED)

    speed_first_degree = 60
    speed_second_degree = 0
    speed_third_degree = 0
    speed_fourth_degree = 0
    speed_fifth_degree = 50
    speed_claw = 100

    hand_speed_factor = 5

    first_degree_txt.config(text=str(speed_first_degree))
    second_degree_txt.config(text=str(speed_second_degree))
    third_degree_txt.config(text=str(speed_third_degree))
    fourth_degree_txt.config(text=str(speed_fourth_degree))
    fifth_degree_txt.config(text=str(speed_fifth_degree))
    claw_txt.config(text=str(speed_claw))

    speed_update_scale.set(hand_speed_factor)

    '''broadrcaster.publish(command_first_degree, int(speed_first_degree))
    time.sleep(.5)
    broadrcaster.publish(command_second_degree, int(speed_second_degree))
    time.sleep(.5)
    broadrcaster.publish(command_third_degree, int(speed_third_degree))
    time.sleep(.5)
    broadrcaster.publish(command_fourth_degree, int(speed_fourth_degree))
    time.sleep(.5)
    broadrcaster.publish(command_fifth_degree, int(speed_fifth_degree))
    time.sleep(.5)
    broadrcaster.publish(command_claw, int(speed_claw))
    time.sleep(.5)'''
    first_degree_inc_update_btn.config(state=ACTIVE)
    first_degree_dec_update_btn.config(state=ACTIVE)
    second_degree_inc_update_btn.config(state=ACTIVE)
    second_degree_dec_update_btn.config(state=ACTIVE)
    third_degree_inc_update_btn.config(state=ACTIVE)
    third_degree_dec_update_btn.config(state=ACTIVE)
    fourth_degree_inc_update_btn.config(state=ACTIVE)
    fourth_degree_dec_update_btn.config(state=ACTIVE)
    fifth_degree_inc_update_btn.config(state=ACTIVE)
    fifth_degree_dec_update_btn.config(state=ACTIVE)
    claw_inc_update_btn.config(state=ACTIVE)
    claw_dec_update_btn.config(state=ACTIVE)
    speed_update_scale.config(state=ACTIVE)
    return


def speed_update_func(val):
    global hand_speed_factor
    hand_speed_factor = int(val)
    return


mainGui = Tk()
broadrcaster = get_broadrcaster()

mainGui.title("extinctCoder")

first_degree_inc_update_btn = (Button(mainGui, state=DISABLED, text="first_degree_inc",
                                      command=first_degree_inc_update_func, height=2, width=20, bg="blue"))
first_degree_dec_update_btn = (Button(mainGui, state=DISABLED, text="first_degree_dec",
                                      command=first_degree_dec_update_func, height=2, width=20, bg="green"))
first_degree_txt = Label(mainGui, text="first_degree")

second_degree_inc_update_btn = Button(mainGui, state=DISABLED, text="second_degree_inc",
                                      command=second_degree_inc_update_func, height=2, width=20, bg="blue")
second_degree_dec_update_btn = Button(mainGui, state=DISABLED, text="second_degree_dec",
                                      command=second_degree_dec_update_func, height=2, width=20, bg="green")
second_degree_txt = Label(mainGui, text="second_degree")

third_degree_inc_update_btn = Button(mainGui, state=DISABLED, text="third_degree_inc",
                                     command=third_degree_inc_update_func, height=2, width=20, bg="blue")
third_degree_dec_update_btn = Button(mainGui, state=DISABLED, text="third_degree_dec",
                                     command=third_degree_dec_update_func, height=2, width=20, bg="green")
third_degree_txt = Label(mainGui, text="third_degree")

fourth_degree_inc_update_btn = Button(mainGui, state=DISABLED, text="fourth_degree_inc",
                                      command=fourth_degree_inc_update_func, height=2, width=20, bg="blue")
fourth_degree_dec_update_btn = Button(mainGui, state=DISABLED, text="fourth_degree_dec",
                                      command=fourth_degree_dec_update_func, height=2, width=20, bg="green")
fourth_degree_txt = Label(mainGui, text="fourth_degree")

fifth_degree_inc_update_btn = Button(mainGui, state=DISABLED, text="fifth_degree_inc",
                                     command=fifth_degree_inc_update_func, height=2, width=20, bg="blue")
fifth_degree_dec_update_btn = Button(mainGui, state=DISABLED, text="fifth_degree_dec",
                                     command=fifth_degree_dec_update_func, height=2, width=20, bg="green")
fifth_degree_txt = Label(mainGui, text="fifth_degree")

claw_inc_update_btn = Button(mainGui, state=DISABLED, text="claw_inc",
                             command=claw_inc_update_func, height=2, width=20, bg="blue")
claw_dec_update_btn = Button(mainGui, state=DISABLED, text="claw_dec",
                             command=claw_dec_update_func, height=2, width=20, bg="green")
claw_txt = Label(mainGui, text="claw")

speed_update_scale = Scale(
    mainGui, state=DISABLED, from_=0, to=10, command=speed_update_func, orient=HORIZONTAL, width=20)
speed_txt = Label(mainGui, text="speed")
sync_with_hand_btn = Button(
    mainGui, text="sync_with_hand", command=sync_func, height=2, bg="purple")

first_degree_inc_update_btn.grid(row=0, column=0)
first_degree_dec_update_btn.grid(row=1, column=0)
first_degree_txt.grid(row=3, column=0)
second_degree_inc_update_btn.grid(row=0, column=1)
second_degree_dec_update_btn.grid(row=1, column=1)
second_degree_txt.grid(row=3, column=1)
third_degree_inc_update_btn.grid(row=0, column=2)
third_degree_dec_update_btn.grid(row=1, column=2)
third_degree_txt.grid(row=3, column=2)
fourth_degree_inc_update_btn.grid(row=0, column=3)
fourth_degree_dec_update_btn.grid(row=1, column=3)
fourth_degree_txt.grid(row=3, column=3)
fifth_degree_inc_update_btn.grid(row=0, column=4)
fifth_degree_dec_update_btn.grid(row=1, column=4)
fifth_degree_txt.grid(row=3, column=4)
claw_inc_update_btn.grid(row=0, column=5)
claw_dec_update_btn.grid(row=1, column=5)
claw_txt.grid(row=3, column=5)

speed_update_scale.grid(row=4, column=0, columnspan=6, sticky='EW')
speed_txt.grid(row=5, column=0, columnspan=6, sticky='EW')
sync_with_hand_btn.grid(row=6, column=0, columnspan=6, sticky='EW')

mainGui.mainloop()
distroy_broadrcaster()
