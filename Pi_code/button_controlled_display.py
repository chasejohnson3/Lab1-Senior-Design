#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi or BeagleBone Black.
from multiprocessing import Process
import RPi.GPIO as GPIO
import time

import Adafruit_CharLCD as LCD
import os
import glob
import time
import MySQLdb

#turn_on_display = 0

def write_to_lcd():
#	global turn_display_on
		r=0
#	while True:
	
        	r += 1
		disPwr = False
        	f=open(DS18B20, "r")
        	data=f.read()
        	f.close()
	
        	(discard, yesorno, otherdata)=data.partition("YES")
        	if not yesorno:
                	yesorno = "NO"
	
        	(discard, sep, reading)=data.partition(" t=")
        	tc = float(reading)/1000.0
        	tf = tc*9.0/5.0 + 32.0
        	
        	#Put any SQL command here - In our case, put sensor data in database
#        	cur.execute("INSERT INTO TempData (idTempData, Temp, Time) VALUES(%s, %s, %s)",(r, tc, r))
        	#cur.execute("INSERT INTO DisplayStatus (Time, dispPwrOnOff) VALUES(%s, %s)", (r,0))
#        	db.commit()
		
		lcd.clear()
		lcd.message("{} {:.2f}C {:.2f}F Working = {}".format(r,tc,tf,yesorno))
        	print("{} {:.2f}C {:.2f}F Working = {}".format(r,tc,tf,yesorno))
	
        	#Delay 1s between readings
        	time.sleep(1.0)
	


def button_callback(channel):
	while 1:
		GPIO.wait_for_edge(26, GPIO.RISING)
		print("turned on")
		write_to_lcd()
		GPIO.wait_for_edge(26, GPIO.FALLING)
		print("turned bad")
		lcd.clear()

if __name__=='__main__':
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
	
	
	
	
	#Set up the database connection
	db = MySQLdb.connect(host="34.68.18.19",
			 	user="root",
			 	passwd="dreamteam1",
			 	db="Lab1")
	#Set up a cursor object so you can accomplish your desired queries
	cur = db.cursor()
	
	
	
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#	GPIO.add_event_detect(26,GPIO.RISING,callback=button_callback)
	#GPIO.add_event_detect(26,GPIO.FALLING, callback=button_callback_2)
	


#	p1 = Process(target=write_to_lcd)
#	p1.start()
	p2 = Process(target=button_callback(26))
	p2.start()

