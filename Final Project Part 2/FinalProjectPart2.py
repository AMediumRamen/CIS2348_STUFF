#Ahmed Rahman PSID# 1820239

import csv
from datetime import datetime

#Opening the Manufacturer CSV and sorting by ID to combine other lists later
with open('FinalProjectManufacturerList.csv','r') as ManufacturerCSV:
    reader = csv.reader(ManufacturerCSV,delimiter=',')
    ManufacturerList=[]
    for row in reader:
        ManufacturerList.append([int(row[0]),row[1],row[2],row[3]])
ManufacturerList.sort(key=lambda a:a[0])

#Opening the PriceList CSV and sorting by ID to combine to Manufacturer List later
with open('FinalProjectPriceList.csv') as PriceListCSV:
    reader = csv.reader(PriceListCSV,delimiter=',')
    PriceList = []
    for row in reader:
        PriceList.append([row[0],row[1]])
PriceList.sort(key=lambda a:a[0])
PricesOnly = [item[1]for item in PriceList]

#Opening the Service Dates List and sorting by ID to combine to Manufacturer list later
with open('FinalProjectServiceDatesList.csv') as ServiceListCSV:
    reader = csv.reader(ServiceListCSV,delimiter=',')
    ServiceList = []
    for row in reader:
        ServiceList.append([row[0],datetime.strptime(row[1],'%m/%d/%Y')])
ServiceList.sort(key=lambda a:a[0])
ServiceDatesOnly = [item[1]for item in ServiceList]

#Appending the Prices from PriceList (made from PriceList CSV) to the Manufacturer List
for i in range(len(ManufacturerList)):
    ManufacturerList[i].append(PricesOnly[i])
#Appending the Service Dates from ServiceList(made from Service Dates CSV) to the Manufacturer List
for i in range(len(ManufacturerList)):
    ManufacturerList[i].append(str(ServiceDatesOnly[i]))

#Making a variable that is a datetime object of today. I used this later to compare Service Dates of items
#to see which items must not be shown
todayDate = str(datetime.today())

#Here I filter out the sublists that have specific values that must not be shown
#in the final result
#for example filtering out the damaged items
for i in ManufacturerList:
    if (i[3]) == 'damaged':
        ManufacturerList.remove(i)
#filtering out the Items that are past service date
for i in ManufacturerList:
    if (i[5]) < str(todayDate):
        ManufacturerList.remove(i)

#Over here I sort the list by Prices since I don't need it sorted by ID anymore
#This is because I needed the list sorted by prices so it shows the most expensive
#items first (according to the instructions)
ManufacturerList.sort(key=lambda a:a[4],reverse=True)

#Over here I make a new list that is formatted based on the desired output in the instructions
#So I removed Damaged indicator and Service dates as per the instructions given
#this list contains only the ID, Manufacturer, Type, and Price
ListToPrint = ManufacturerList
for i in ListToPrint:
    del i[3]
    del i[4]

#Over here I make a list of just Manufacturers and types
#This is used to filter out the words I need from the user input and ignore the ones I don't
OnlyManufacturer = [item[1]for item in ManufacturerList]
OnlyTypes = [item[2]for item in ManufacturerList]


#AIGHT main part Let's go
#first take an input to start off the process
inpt=input('Enter brand and type of item:')
#until the user inputs 'q' keep the while loop going
while inpt != "q":
    userinput = inpt.split()#splits the input into words which I will iterate through
    yikes1 = ''#Empty string varible which will take the Manufacturer from user input
    yikes2 = ''#Empty string variable which will take the type from user input

    #Initialized this so I can get one value as a result
    #since the lists are sorted by Price at this moment, it will output the most expensive item
    donefornow = False

    #Looking to see if any of the words in the user input is in the lists of manufacturers
    #and assigns to yikes1
    for c in userinput:
        if c in OnlyManufacturer:
            yikes1 += c

    # Looking to see if any of the words in the user input is in the lists of types
    # and assigns to yikes2
    for c in userinput:
        if c in OnlyTypes:
            yikes2 += c
    #These are here to get assign indexes of types of manufacturers
    yikers = 0
    yikers2= 0

    #Nothing in inventory if the no important words (manufacturers available or types available) were caught.
    #So with the help of the code above this segment should return "No such item in inventory" if user input does
    #not exist in inventory
    if yikes1 == '' or yikes2 =='':
        print("No such item in inventory")
    #If yikes1 and yikes2 actually catch something, then:
    else:
        #finds the index of the item desired by user (based on type and manufacturer)
        #also changes donefornow to True
        #so basically should only return one item and the similar item
        for item in ManufacturerList:
            if item[2]== yikes2 and item[1]==yikes1:
                yikers = ManufacturerList.index(item)
                donefornow = True

        #find the index of another item that has the same type but not the same manufacturer
        for item in ManufacturerList:
            if item[2]== yikes2 and item[1] != yikes1:
                yikers2 = ManufacturerList.index(item)
        #If done for now is True at this point, then print the item and the similar item
        if donefornow == True:
            print("Your item is:",ListToPrint[int(yikers)])
            print("You may, also, consider:",ListToPrint[int(yikers2)])

        #otherwise, nothing was found so print that as well
        else:
            print("No such item in inventory")

    #keep triggering input till the user enters 'q'
    inpt = input('Enter brand and type of item:')