#!/usr/bin/env python
import os
import glob
import time

DS18B20="/sys/bus/w1/devices/28-021316acc9aa/w1_slave"

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

	print("{} {:.2f}C {:.2f}F Working = {}".format(r,tc,tf,yesorno))
	time.sleep(1.0)
