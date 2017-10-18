import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================

nametable = "CREATE TABLE peepz (name TEXT, age INTEGER, id INTEGER)"          #put SQL statement in this string
c.execute(nametable)    #run SQL statement
coursestable = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)"          #put SQL statement in this string
c.execute(coursestable)    #run SQL statement

peepz = csv.DictReader(open("peeps.csv"))
for row in peepz:
	name = row['name']
	age = row['age']
	id = row['id']
	adduser = "INSERT INTO peepz VALUES (%s, '%s', %s);"%(age, name, id)
	c.execute(adduser)

courses = csv.DictReader(open("courses.csv"))
for row in courses:
    code = row['code']
    mark = row['mark']
    id = row['id']
    addcourse = "INSERT INTO courses VALUES ('%s', %s, %s);"%(code, mark, id)
    c.execute(addcourse)

#==========================================================
db.commit() #save changes
db.close()  #close database
