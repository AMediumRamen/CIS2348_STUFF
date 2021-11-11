#Ahmed Rahman PSID:1820239

listMaker = input()
stringList = listMaker.split()
stringDictionary = {}

for i in stringList:
    if i in stringDictionary:
        stringDictionary[i] += 1
    else:
        stringDictionary[i] = 1
for word in stringList:
    for keys in stringDictionary:
        print(keys,stringDictionary.get(keys))