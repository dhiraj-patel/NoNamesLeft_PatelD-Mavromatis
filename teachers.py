from pymongo import MongoClient
import csv

#-------- CSV stuff --------

#open csv
fObj = open("teachers.csv")
#read csv
d=csv.DictReader(fObj)

#-------- connecting to mongo stuf --------

c = MongoClient('149.89.150.100')
ourDB = c.noNamesLeft

students = ourDB.students.find()

toIns = []

for i in d:
    #init
    teacher = {}

    #teacher info
    for j in i:
        teacher[j] = i[j]

    #init
    print ourDB.students.find({key: {"$exists": True}})

    #ourDB.teachers.insert_one(teacher)
