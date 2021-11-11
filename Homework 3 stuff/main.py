# Ahmed Rahman PSID:1820239
listMaker = input()
listToFilter = listMaker.split()
yikersList=[]
for i in listToFilter:
    if int(i)>0:
        yikersList.append(int(i))


yikersList.sort()

for i in yikersList:
    print(i,end=' ')
