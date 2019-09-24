#Joshua Deutsch
#Python Script to establish database connection
#!/usr/bin/python
# This library is required to connect to a MySQL database
import MySQLdb

#Set up the database connection
db = MySQLdb.connect(host="34.68.18.19",
			 user="root",
			 passwd="dreamteam1",
			 db="Lab1")
#Set up a cursor object so you can accomplish your desired queries
cur = db.cursor()
#Put any SQL command here
cur.execute("INSERT INTO TempData (idTempData, Temp, Time) VALUES(4, 100, 30)")
db.commit()


#A simple print showing that we've successfully connected to the database
#for row in cur.fetchall():
#	print " temp =" + row[2]




db.close()




