#Ahmed Rahman PSID:1820239
import csv
ManList = csv.reader(open('ManufacturerList.csv'))
ManDict = {}
for row in ManList:
    key = row[0]
    ManDict[key] = row[1:2]

PriceList = csv.reader(open('PriceList.csv'))
PriceDict = {}
for row in PriceList:
    key = row[0]
    PriceDict[key]=row[1]

ServiceDatesList = csv.reader(open('ServiceDatesList.csv'))
ServiceDatesDict = {}
for row in ServiceDatesList:
    key = row[0]
    ServiceDatesDict[key]=row[1]

print(ManDict)










