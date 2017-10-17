import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================

nametable = ("CREATE TABLE peepz (name TEXT, age INTEGER, id INTEGER)")          #put SQL statement in this string
c.execute(nametable)    #run SQL statement
peepz = csv.DictReader(open("peeps.csv"))
for row in peepz:
	add_row = 'INSERT INTO peepz VALUES ("' + row["name"] + '",' + row["age"] + "," + row["id"] + ")"
	c.execute(add_row)

coursestable = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)"          #put SQL statement in this string
c.execute(coursestable)    #run SQL statement
courses = csv.DictReader(open("courses.csv"))
for row in peepz:
	add_row = 'INSERT INTO courses VALUES ("' + row["code"] + '",' + row["mark"] + "," + row["id"] + ")"
	c.execute(add_row)

#==========================================================
db.commit() #save changes
db.close()  #close database
