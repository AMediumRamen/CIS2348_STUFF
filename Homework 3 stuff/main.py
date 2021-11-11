#Ahmed Rahman PSID:1820239

listMaker = input()
stringList = listMaker.split()

for string in stringList:
    yikes = stringList.count(string)
    print(string,yikes)