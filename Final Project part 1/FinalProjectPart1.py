#Ahmed Rahman PSID:1820239
import csv
import datetime


yikes = open('FinalProjectFullInventory.csv','w')
yikes2 = open('FinalProjectLaptopInventory.csv','w')
yikes3 = open('FinalProjectPhoneInventory.csv','w')
yikes4 = open('FinalProjectTowerInventory.csv','w')
yikes5 = open('FinalProjectPastServiceDateInventory.csv','w')
yikes6 = open('FinalProjectDamagedInventory.csv','w')

with open('FinalProjectManufacturerList.csv','r') as Man_csv:
    reader = csv.reader(Man_csv,delimiter=',')
    ManList=[]
    for row in reader:
        ManList.append([int(row[0]),row[1],row[2],row[3]])


IDList = []
for sublist in ManList:         #List of IDs Only that I can iterate through later
    IDList.append(sublist[0])
ID = tuple(IDList)              #Had to change to a tuple to avoid errors


ManDict={}                      #Dictionary of Manufacturers will be used to get values while iterating through ID List
for row in ManList:
    key = int(row[0])
    ManDict[key] = row[1]



typeDict = {}   #Dictionary of types will be used to get values while iterating through ID List
for row in ManList:
    key = int(row[0])
    typeDict[key] = row[2]



PriceList = csv.reader(open('FinalProjectPriceList.csv')) #Dictionary of Prices will be used to get values while iterating through ID List
PriceDict = {}
for row in PriceList:
    key = int(row[0])
    PriceDict[key]=int(row[1])


ServiceDatesList = csv.reader(open('FinalProjectServiceDatesList.csv'))#Dictionary of Serice Dates will be used to get values while iterating through ID List
ServiceDatesDict = {}
for row in ServiceDatesList:
    key = int(row[0])
    ServiceDatesDict[key]=datetime.strptime(row[1],'%m/%d/%Y')

DamagedDict={}# Dictionary of Damaged items will be used to get values while iterating through ID List
for row in ManList:
    key = int(row[0])
    DamagedDict[key]=row[3]

sortedArray = []#Empty List to put x in (need it to sort later)
for ids in ID:
    x = list((ids,ManDict.get(ids),typeDict.get(ids),PriceDict.get(ids),str(ServiceDatesDict.get(ids)),DamagedDict.get(ids)))
    sortedArray.append(x)

sortedArray.sort(key=lambda a:a[1])
i = 0
while i < len(sortedArray):
    yikes.write(str(sortedArray[i]))
    yikes.write('\n')
    i += 1

#dictionaries of specific conditions IDs
laptop_ids= [k for k, v in typeDict.items() if v == 'laptop']
phone_ids = [k for k, v in typeDict.items() if v == 'phone']
tower_ids = [k for k, v in typeDict.items() if v == 'tower']
x= datetime.datetime.today()
service_ids = [k for k, v in ServiceDatesDict.items() if v < x]
damaged_ids = [k for k, v in DamagedDict.items() if v == 'damaged']
#dictionaries of specific conditions IDs

#laptops
sortedLaptops=[]
for ids in laptop_ids:
    laptop_list = list((ids,ManDict.get(ids),PriceDict.get(ids),str(ServiceDatesDict.get(ids)),DamagedDict.get(ids)))
    sortedLaptops.append(laptop_list)
sortedLaptops.sort(key=lambda  a:a[0])
i=0
while i< len(sortedLaptops):
    yikes2.write(str(sortedLaptops[i]))
    yikes2.write('\n')
    i +=1
#laptops

#phones
sortedPhones=[]
for ids in phone_ids:
    phone_list= list((ids,ManDict.get(ids),PriceDict.get(ids),str(ServiceDatesDict.get(ids)),DamagedDict.get(ids)))
    sortedPhones.append(phone_list)
sortedPhones.sort(key=lambda  a:a[0])
i=0
while i< len(sortedPhones):
    yikes3.write(str(sortedPhones[i]))
    yikes3.write('\n')
    i +=1
#phones

#towers
sortedTowers=[]
for ids in tower_ids:
    tower_list= list((ids,ManDict.get(ids),PriceDict.get(ids),str(ServiceDatesDict.get(ids)),DamagedDict.get(ids)))
    sortedTowers.append(tower_list)
sortedTowers.sort(key=lambda  a:a[0])
i=0
while i< len(sortedTowers):
    yikes4.write(str(sortedTowers[i]))
    yikes4.write('\n')
    i +=1
#towers

#past service date
sortedPastService=[]
for ids in service_ids:
    serviceList= list((ids,ManDict.get(ids),typeDict.get(ids),PriceDict.get(ids),str(ServiceDatesDict.get(ids)),DamagedDict.get(ids)))
    sortedPastService.append(serviceList)
sortedPastService.sort(key=lambda  a:a[4])
i=0
while i< len(sortedPastService):
    yikes5.write(str(sortedPastService[i]))
    yikes5.write('\n')
    i +=1
#past service date
#damaged inventory
sortedDamaged=[]
for ids in damaged_ids:
    damagedList= list((ids,ManDict.get(ids),typeDict.get(ids),PriceDict.get(ids),str(ServiceDatesDict.get(ids))))
    sortedDamaged.append(damagedList)
sortedDamaged.sort(key=lambda  a:a[3],reverse=True)
i=0
while i< len(sortedDamaged):
    yikes6.write(str(sortedDamaged[i]))
    yikes6.write('\n')
    i +=1


#damaged inventory



















