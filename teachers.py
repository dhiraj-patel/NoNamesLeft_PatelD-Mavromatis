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

for i in d:
    #init
    teacher = {}

    #teacher info
    for j in i:
        teacher[j] = i[j]

    #init
    key = teacher['code']
    students = ourDB.students.find({key: {"$exists": True}})
    for j in students:
        print j

    #ourDB.teachers.insert_one(teacher)
