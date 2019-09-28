#############################################################################################
#					Multithreaded.py
#############################################################################################
#!/usr/bin/python
#  	               			IMPORT LIBRARIES
from multiprocessing import Process
import time
import RPi.GPIO as GPIO
import Adafruit_CharLCD as LCD
import os
import glob
import MySQLdb
#  	               			DEFINE MACROS
writing_to_LCD = 0 #Not writing(0) or writing(1) to the LCD
backlight = 0 #Backlight off(0) or Backlight on (1)
r = 0 # Current temperature sample
tc = 0 # Current temperature in celsius
tf = 0 # Global varaible for fahrenheit
#  	               			CONFIGURE DATABASE
db = MySQLdb.connect(host="34.68.18.19",
			 	user="root",
			 	passwd="dreamteam1",
			 	db="Lab1")
cur = db.cursor()
#  	               			CONFIGURE LCD
lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 4
lcd_columns = 16 # Define LCD column and row size for 16x2 LCD.
lcd_rows    = 2	
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           	lcd_columns, lcd_rows, lcd_backlight) # Initialize the LCD using the pins above.
#  	               			CONFIGURE GPIO FOR BUTTON
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#  	               			SPECIFY THERMOCOUPLE BUS
DS18B20="/sys/bus/w1/devices/28-021316acc9aa/w1_slave"

##############################################################################
#Function to handle button press
##############################################################################
def button_callback(channel):
	global writing_to_LCD
	while 1:
		GPIO.wait_for_edge(26, GPIO.RISING)
	  	writing_to_LCD = 1
	      	lcd.initial_backlight = writing_to_LCD
		GPIO.wait_for_edge(26, GPIO.FALLING)
	      	writing_to_LCD = 0
		lcd.initial_backlight = writing_to_LCD
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
#	    cur.execute("INSERT INTO DisplayStatus (Time, dispPwrOnOff) VALUES(%s, %s)", (r,0))
	    db.commit()

	    if writing_to_LCD:
		write_to_LCD()
	    time.sleep(1.0)

################################################################################      
#Function to update backlight
################################################################################    
#def update_backlight():	
	
	
	

################################################################################      
#Main program
################################################################################      
if __name__=='__main__':
	p1 = Process(target=read_temperature)
	p1.start()	
	p2 = Process(target=button_callback(26))
	p2.start()
  
  
  
