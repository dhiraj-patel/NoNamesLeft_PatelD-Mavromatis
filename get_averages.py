from pymongo import MongoClient


c = MongoClient("149.89.150.100")
ourDB = c.noNamesLeft
classes = ["softdev","systems","ceramics","greatbooks"]

d = ourDB.students.find()

for i in d:
    average = 0
    numClass = 0
    for j in i:
        if j in classes:
            average += int(i[j])
            numClass +=1 
    print "name: %s , id: %d , average: %d"%(str(i['name']),int(i['id']),average) 



