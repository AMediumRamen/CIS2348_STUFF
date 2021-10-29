#Ahmed Rahman PSID:1820239
ManList = list(open('ManufacturerList.csv','r'))
PriceList = list(open('PriceList.csv','r'))
ServiceDatesList = list(open('ServiceDatesList.csv','r'))

def CovertToDict(list):
    iterate = iter(list)
    converted = dict(zip(iterate,iterate))
    return converted
PriceDict = CovertToDict(PriceList)
print(PriceDict)





