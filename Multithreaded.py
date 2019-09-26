#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi or BeagleBone Black.
#Libraries
from multiprocessing import Process
import RPi.GPIO as GPIO
import time
import Adafruit_CharLCD as LCD
import os
import glob
import time
import MySQLdb

##Macros
writing_to_LCD = 0
backlight = 0 #TO DO: Turn Backlight Off
r = 0 # Global variable for current sample
tc = 0 # Global variable for celsius
tf = 0 # Global varaible for farenheit

#Configure database
db = MySQLdb.connect(host="34.68.18.19",
			 	user="root",
			 	passwd="dreamteam1",
			 	db="Lab1")
cur = db.cursor()

#Configure LCD for Raspberry Pi
lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 4
	
# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2
	
# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           	lcd_columns, lcd_rows, lcd_backlight)

#Setup GPIO for button
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#Define Data Bus
DS18B20="/sys/bus/w1/devices/28-021316acc9aa/w1_slave"

##############################################################################
#Function to handle button press
##############################################################################

def button_callback(channel):
	global writing_to_LCD
  while 1:
		GPIO.wait_for_edge(26, GPIO.RISING)
		  writing_to_LCD = 1
      #Turn Backlight On
		GPIO.wait_for_edge(26, GPIO.FALLING)
      writing_to_LCD = 0
      #Turn Backlight Off
      
      
################################################################################      
#Function to print to LCD
################################################################################      
def write_to_lcd():
  lcd.clear()
	lcd.message("{} {:.2f}C {:.2f}F Working = {}".format(r,tc,tf,yesorno))
  print("{} {:.2f}C {:.2f}F Working = {}".format(r,tc,tf,yesorno))
	
################################################################################      
#Function to read and log temperature
################################################################################      
def read_temperature():
global r, tc, tf 
while 1:
    r+=1
    f=open(DS18B20, "r")
    data=f.read()
    f.close()

    (discard, yesorno, otherdata)=data.partition("YES")
    if not yesorno:
      yesorno = "NO"

    (discard, sep, reading)=data.partition(" t=")
    tc = float(reading)/1000.0
    tf = tc*9.0/5.0 + 32.0  

    cur.execute("INSERT INTO TempData (idTempData, Temp, Time) VALUES(%s, %s, %s)",(r, tc, r))
    cur.execute("INSERT INTO DisplayStatus (Time, dispPwrOnOff) VALUES(%s, %s)", (r,0))
    db.commit()
    
    if writing_to_LCD:
      write_to_LCD()
    
    time.sleep(1.0)
  
################################################################################      
#Main program
################################################################################      
if __name__=='__main__':
  p1 = Process(target=read_temperature)
  p1.start()
	p2 = Process(target=button_callback(26))
	p2.start()
  
  
  
