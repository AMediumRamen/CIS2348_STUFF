#Ahmed Rahman PSID# 1820239
#Used Dictionaries for part 1. For part 2 trying to take a different approach
#hopefully a class
#one function to return value based on input
#one function to return similar item of different brand based on input
import csv
from datetime import datetime


with open('FinalProjectPart2ManufacturerList.csv','r') as ManufacturerCSV:
    reader = csv.reader(ManufacturerCSV,delimiter=',')
    ManufacturerList=[]
    for row in reader:
        ManufacturerList.append([int(row[0]),row[1],row[2],row[3]])
ManufacturerList.sort(key=lambda a:a[0])


with open('FinalProjectPart2PriceList.csv') as PriceListCSV:
    reader = csv.reader(PriceListCSV,delimiter=',')
    PriceList = []
    for row in reader:
        PriceList.append([row[0],row[1]])
PriceList.sort(key=lambda a:a[0])
PricesOnly = [item[1]for item in PriceList]


with open('FinalProjectPart2ServiceDatesList.csv') as ServiceListCSV:
    reader = csv.reader(ServiceListCSV,delimiter=',')
    ServiceList = []
    for row in reader:
        ServiceList.append([row[0],datetime.strptime(row[1],'%m/%d/%Y')])
ServiceList.sort(key=lambda a:a[0])
ServiceDatesOnly = [item[1]for item in ServiceList]


for i in range(len(ManufacturerList)):
    ManufacturerList[i].append(PricesOnly[i])

for i in range(len(ManufacturerList)):
    ManufacturerList[i].append(str(ServiceDatesOnly[i]))
todayDate = str(datetime.today())


for i in ManufacturerList:
    if (i[3]) == 'damaged':
        ManufacturerList.remove(i)
for i in ManufacturerList:
    if (i[5]) < str(todayDate):
        ManufacturerList.remove(i)

ManufacturerList.sort(key=lambda a:a[4],reverse=True)


OnlyManufacturer = [item[1]for item in ManufacturerList]
OnlyTypes = [item[2]for item in ManufacturerList]

yikes1 = ''
yikes2 = ''
indexofyikes1 = ''
indexofyikes2 =''
userinput=input('Enter brand and type of item:').split()
for c in userinput:
    if c in OnlyManufacturer:
        yikes1 += c
        indexofyikes1 = OnlyManufacturer.index(c)

for c in userinput:
    if c in OnlyTypes:
        yikes2 += c
        indexofyikes2 = OnlyTypes.index(c)
yikers = ''
if yikes1 == '' or yikes2 =='':
    print("No such item in inventory ")
elif indexofyikes1 != indexofyikes2:
    print("bruh")

else:
    for item in ManufacturerList:
        if item[2]== yikes2 and item[1]==yikes1:
            yikers = ManufacturerList.index(item)
    print(ManufacturerList[yikers])
