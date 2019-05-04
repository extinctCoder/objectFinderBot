# Import necessary libraries.
from time import sleep

from Bluetin_Echo import Echo

# Define pin constants
TRIGGER_PIN_1 = 11
ECHO_PIN_1 = 13
TRIGGER_PIN_2 = 19
ECHO_PIN_2 = 21

# Initialise two sensors.
echo = [Echo(TRIGGER_PIN_1, ECHO_PIN_1), Echo(TRIGGER_PIN_2, ECHO_PIN_2)]


def main():
    sleep(0.1)
    for counter in range(1, 6):
        for counter2 in range(0, len(echo)):
            result = echo[counter2].read('cm', 3)
            print('Sensor {} - {} cm'.format(counter2, round(result, 2)))

    echo[0].stop()


if __name__ == '__main__':
    main()
