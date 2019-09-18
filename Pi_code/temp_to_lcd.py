#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi or BeagleBone Black.
import time

import Adafruit_CharLCD as LCD
import os
import glob
import time

DS18B20="/sys/bus/w1/devices/28-021316acc9aa/w1_slave"

# Raspberry Pi pin configuration:
lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 4


#initialize LCD
# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

# Print a two line message
lcd.message('Let\'s get\nstarted')
time.sleep(5.0)

r=0

while True:

        r += 1
        f=open(DS18B20, "r")
        data=f.read()
        f.close()

        (discard, yesorno, otherdata)=data.partition("YES")
        if not yesorno:
                yesorno = "NO"

        (discard, sep, reading)=data.partition(" t=")
        tc = float(reading)/1000.0
        tf = tc*9.0/5.0 + 32.0

	lcd.clear()
	lcd.message("{} {:.2f}C {:.2f}F Working = {}".format(r,tc,tf,yesorno))
        print("{} {:.2f}C {:.2f}F Working = {}".format(r,tc,tf,yesorno))
        time.sleep(1.0)

