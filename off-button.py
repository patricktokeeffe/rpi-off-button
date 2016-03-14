#!/usr/bin/python
#
# Listen for BCM 21--Gnd closed circuit, then shut down system
#
# Patrick O'Keeffe
#

import RPi.GPIO as GPIO
import time
import os

OFF_PIN = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(OFF_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def shutdown(channel):
    for i in range (30):
        time.sleep(0.1)
        if GPIO.input(OFF_PIN):
            return # button was released
    os.system('sudo shutdown -h now "Off button pressed!"')

GPIO.add_event_detect(21, GPIO.FALLING, callback=shutdown, bouncetime=200)
while(True):
    time.sleep(1)

