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
    me = {}
    for j in i:
        me[j] = i[j]
    me['student'] = []
    for j in students:
        if (me['code'] in j):
            me['student'].append(str(j['name'])
    toIns.append(me)

ourDB.teachers.insert_many(toIns)
