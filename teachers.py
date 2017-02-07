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
    me = {}

    #teacher info
    for j in i:
        me[j] = i[j]

    #init
    me['student'] = []

    #student info
    for j in students:
        if (me['code'] in j):
            me['student'].append(str(j['name'])

    print me

ourDB.teachers.insert_many(toIns)
