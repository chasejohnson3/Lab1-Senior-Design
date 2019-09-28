
#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi or BeagleBone Black.
import time

import Adafruit_CharLCD as LCD
import os
import glob
import time
import MySQLdb

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

r=0
while True:

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
    #    cur.execute("INSERT INTO TempData (idTempData, Temp, Time) VALUES(%s, %s, %s)",(r, tc, r))
        
     #   db.commit()
	
	cur.execute("select * from Lab1.DisplayStatus")
	resultSet = cur.fetchall()
	for row in resultSet:
		print row[0], row[1]
	db.commit()
	
	
	if(row[1]):
		lcd.clear()
		lcd.message("{} {:.2f}C {:.2f}F Working = {}".format(r,tc,tf,yesorno))
        	print("{} {:.2f}C {:.2f}F Working = {}".format(r,tc,tf,yesorno))
	else:
		lcd.clear()

        #Delay 1s between readings
        time.sleep(1.0)


