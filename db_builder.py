from pymongo import MongoClient
import csv

c = MongoClient("lisa.stuy.edu")
ourDB = c.NoNamesLeft

#-------- CSV stuff --------
#open csv
fObj = open("peeps.csv")
#read csv
d=csv.DictReader(fObj)

for i in d:
    ourDB.foo.insert_one(i)
