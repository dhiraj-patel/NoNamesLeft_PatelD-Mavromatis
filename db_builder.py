from pymongo import MongoClient
import csv

#-------- CSV stuff --------

#open csv
fObj = open("peeps.csv")
#read csv
d=csv.DictReader(fObj)

obj2 = open('courses.csv')
temp = csv.DictReader(obj2)

#bc DictReader can only be iterated over once
d2 = []
for j in temp:
    d2.append(j)

#-------- make list (dic) to be inserted --------

dic = []

for i in d:
    combine = {}
    for j in i:
        combine[j] = i[j]
    for j in d2:
        if (combine['id'] == j['id']):
            combine[j['code']] = j['mark']
    dic.append(combine)

fObj.close()
obj2.close()


#-------- mongo stuf --------

c = MongoClient('lisa.stuy.edu')
ourDB = c.noNamesLeft

for i in dic:
    #print type(i)
    ourDB.students.insert_one(i)
#ourDB.students.insert_many(dic)
