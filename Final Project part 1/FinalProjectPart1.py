#Ahmed Rahman PSID:1820239
import csv
import datetime

yikes = open('FullInventory.csv','w')

with open('ManufacturerList.csv','r') as Man_csv:
    reader = csv.reader(Man_csv,delimiter=',')
    ManList=[]
    for row in reader:
        ManList.append([int(row[0]),row[1],row[2],row[3]])


IDList = []
for sublist in ManList:         #List of IDs Only
    IDList.append(sublist[0])
ID = tuple(IDList)              #Had to change to a tuple to avoid errors


ManDict={}                      #Dictionary of Manufacturers
for row in ManList:
    key = int(row[0])
    ManDict[key] = row[1]



typeDict = {}   #Dictionary of types
for row in ManList:
    key = int(row[0])
    typeDict[key] = row[2]



PriceList = csv.reader(open('PriceList.csv'))    #Dictionary of Prices
PriceDict = {}
for row in PriceList:
    key = int(row[0])
    PriceDict[key]=int(row[1])


ServiceDatesList = csv.reader(open('ServiceDatesList.csv'))   #Dictionary of Serice Dates
ServiceDatesDict = {}
for row in ServiceDatesList:
    key = int(row[0])
    ServiceDatesDict[key]=datetime.datetime.strptime(row[1],'%m/%d/%Y')

DamagedDict={}
for row in ManList:
    key = int(row[0])
    DamagedDict[key]=row[3]

sortedArray = []
for ids in ID:
    x = list((ids,ManDict.get(ids),typeDict.get(ids),PriceDict.get(ids),ServiceDatesDict.get(ids),DamagedDict.get(ids)))
    sortedArray.append(x)

sortedArray.sort(key=lambda a:a[1])
print(sortedArray)

#for ids in ID:
#    x1 = list([ids,ManDict.get(ids),typeDict.get(ids),PriceDict.get(ids),ServiceDatesDict.get(ids),DamagedDict.get(ids)])
#    fullArray = [x1]
#    fullArray.sort(key=lambda a:a[1])
#    print(fullArray)
#    yikes.write(str(fullArray))
#    yikes.write('\n')



























