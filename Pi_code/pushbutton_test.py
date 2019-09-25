#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi or BeagleBone Black.
import time

#import Adafruit_CharLCD as LCD
import os
import glob
import time
import MySQLdb
import RPi.GPIO as GPIO

#DS18B20="/sys/bus/w1/devices/28-021316acc9aa/w1_slave"



#define i/o pin for switch
#def button_callback(channel):
#    print("Button was Pushed")


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(26)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)